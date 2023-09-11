import requests
import json
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()
MYSQL_CONNECTOR_URL = chat_id = os.environ.get("RESOURCE_URL")


def query(dataframe):
    year = dt.strftime('%Y')
    week = dt.strftime("%V")
    file_name = f"News_Week_{week}_{year}"
    if os.path.exists(file_name):
        dataframe.to_csv(file_name, mode='a', header=None, index=False)
    else:
        dataframe.to_csv(file_name, index=False)
