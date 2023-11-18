import requests
import json
import os 
from pprint import pprint
from autoscraper import AutoScraper

def news():
    subscription_key = "c4ca97af53ae47f9a0f05f3cbd92495b"
    endpoint = "https://api.bing.microsoft.com/v7.0/search"

    # Query term(s) to search for. 
    search_term = "accessibility travel"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key, "Accept-Language": "en-gb"}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "cc": "SG", "mkt": "SG", "count": 100}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    for res in search_results["webPages"]["value"]:
        pass
    # print(search_results["webPages"]["totalEstimatedMatches"])

def post():
    url = "http://127.0.0.1:5000/requirement"
    payload = {
        "input": "Mongolia"
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Request successful")
        print("Response body:")
        print(response.text)
    else:
        print("Request failed with status code:", response.status_code)

def get():
    url = "http://127.0.0.1:5000"

    response = requests.get(url)

    if response.status_code == 200:
        print("Request successful")
        print("Response body:")
        print(response.text)
    else:
        print("Request failed with status code:", response.status_code)


def test_json():
    with open('data/news_text_AR.json', 'r') as openfile:
        json_object = json.load(openfile)
    print(json_object)
    print(type(json_object))

test_json()