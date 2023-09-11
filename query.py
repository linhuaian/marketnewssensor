import requests
import json
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
MYSQL_CONNECTOR_URL = chat_id = os.environ.get("RESOURCE_URL")


def query(type, statement):
    file_name = ""
