import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
MYSQL_CONNECTOR_URL = chat_id = os.environ.get("RESOURCE_URL")


def query(type, statement):
    payload = {
        'statement': statement,
        'type': type
    }
    if type == "select":
        response = requests.post(MYSQL_CONNECTOR_URL, data=json.dumps(payload))
        if not response.json():
            return []
        data = json.loads(response.json()['body'])
        json_data = data['result']
        return json_data
    elif type == "other":
        requests.post(MYSQL_CONNECTOR_URL, data=json.dumps(payload))
        return []