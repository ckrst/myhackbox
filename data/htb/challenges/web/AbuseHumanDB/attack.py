import requests
import json
import re

url = "http://127.0.0.1:1337"


def post_abusive_url(abusive_url):
    """
    POSTs an abusive URL to the AbuseHumanDB API.
    """
    data = {
        "url": abusive_url
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url + "/api/entries", data=json.dumps(data), headers=headers)
    print(response.text)

abusive_url = "http://localhost/entries"
post_abusive_url(abusive_url)  

