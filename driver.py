from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime, timezone
from config import news_channels
from user_agents import agents
from query import query
import random
import time




chrome_options = Options()
chrome_options.add_argument(f"window-size={random.randint(500, 1000)},{random.randint(500, 1000)}")
chrome_options.add_argument(f"user-agent={random.choice(agents)}")
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])


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
        query("other", statement)
        pass


class Channel(Uploader):

    RESULT = []

    def __init__(self, channel, url, sections, news_attr, news_attr_name):
        self.channel = channel
        self.url = url
        self.sections = sections
        self.news_attr = news_attr
        self.news_attr_name = news_attr_name
        self.driver = webdriver.Chrome(options=chrome_options)
        super().__init__(query)

    def scrap_content(self):
        random.shuffle(self.sections)
        print(self.sections)
        for section in self.sections:
            if section == "main":
                self.driver.get(f"{self.url}")
            else:
                self.driver.get(f"{self.url}{section}")
            time.sleep(random.randint(1, 50) * 0.1)
            headlines = self.driver.find_elements_by_xpath(f'//*[@{self.news_attr}="{self.news_attr_name}"]')
            headlines = [x.text for x in headlines if x.text]
            super().upload_sql(headlines, self.channel, section)
            time.sleep(random.randint(100, 300))
            self.restart_driver()

    def restart_driver(self):
        self.driver.quit()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": f"{random.choice(agents)}",
                                                                    "platform": "Windows"})  # Randomize user agent
def scrap():
    try:
        channels = [Channel(x[0], x[1], x[2], x[3], x[4]) for x in news_channels]
        for chan in channels:
            chan.scrap_content()
        print("Scrap done!")
    except Exception as e:
        print(str(e))
