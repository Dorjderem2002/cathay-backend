import requests
import json
import os 
from pprint import pprint

def news():
    

    '''
    This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
    '''
    subscription_key = "c4ca97af53ae47f9a0f05f3cbd92495b"
    endpoint = "https://api.bing.microsoft.com/v7.0/search"

    # Query term(s) to search for. 
    search_term = "accessibility travel"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    for res in search_results["webPages"]["value"]:
        print(res.keys())
    
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


news()