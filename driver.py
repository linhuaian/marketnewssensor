from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from datetime import datetime, timezone
from config import news_channels, output_columns
from user_agents import agents
from query import query
import random
import time
import os

PROJECT_ROOT = os.path.abspath(os.getcwd())

options = FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}



class Uploader:

    def __init__(self, q):
        self.query = q
        pass

    def upload_sql(self, headlines, channel, section):
        print(f"Number of headlines is {len(headlines)}")
        dt = datetime.now().replace(tzinfo=timezone.utc)
        date = dt.strftime('%Y-%m-%d')
        time = dt.strftime('%H:%M:%S')
        week = dt.strftime("%V")
        headlines = [headline.replace('"', "'") for headline in headlines]
        statement = "insert ignore into headlines (date, week, time, headline, news_channel, section) values "
        headlines = [f'("{date}", "{week}", "{time}", "{headline}", "{channel}", "{section}")' for headline in headlines]
        statement = statement + ",".join(headlines)
        self.query("other", statement)
        pass


class Channel(Uploader):
    """
    A channel object. Simply change channel, url, section, news_attr_dict to scrap the news from different channels.
    Modified the channel in config.py, following format of previous channels strictly.
    """
    RESULT = []

    def __init__(self, channel, url, sections, news_attr_dict, copt=options):
        if not sections:
            sections = ["main"]
        self.driver = None
        self.channel = channel
        self.url = url
        self.sections = sections
        self.news_attr_dict = news_attr_dict
        self.copt = copt
        super().__init__(query)

    def scrap_content(self, driver):
        random.shuffle(self.sections)
        print(self.sections)
        for section in self.sections:
            if not self.url:
                print(f"URL has problem for {self.channel}")
                break
            if section == "main":
                driver.get(f"{self.url}")
            else:
                driver.get(f"{self.url}{section}")
            time.sleep(random.randint(1, 50) * 0.1)  # Time interval is random so that we act like real human being
            for news_attr, news_attr_names in self.news_attr_dict.items():
                for news_attr_name in news_attr_names:
                    try:
                        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, f'//*[@{news_attr}="{news_attr_name}"]')))
                        headlines = driver.find_elements_by_xpath(f'//*[@{news_attr}="{news_attr_name}"]')
                        headlines = [x.text for x in headlines if x.text]
                        super().upload_sql(headlines, self.channel, section)
                        time.sleep(random.randint(10, 30))    # Time interval is random so that we act like real human
                    except Exception as e:
                        print(f"Loading timeout for {self.channel} {news_attr}: {str(e)}...")
                        continue

def scrap():
    try:
        channels = [Channel(x[0], x[1], x[2], x[3]) for x in news_channels]
        random.shuffle(channels)
        driver = webdriver.Firefox(options=options, executable_path=f"{PROJECT_ROOT}/geckodriver")
        for chan in channels:
            try:
                chan.scrap_content(driver)
            except Exception as e:
                print(str(e))
                driver.quit()
                driver = webdriver.Firefox(options=options, executable_path=f"{PROJECT_ROOT}/geckodriver")
        driver.quit()
        print("Scrap done!")
    except Exception as e:
        print(str(e))
