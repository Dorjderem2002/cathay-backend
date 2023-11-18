import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import json
import re

def travel_requirement(country):
    country = country.lower().capitalize()
    base_url = f'https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/{country}.html'
    
    opener = urllib.request.FancyURLopener({})
    f = opener.open(base_url)
    content = f.read()
    bs = BeautifulSoup(content, 'html.parser')
    res = bs.find_all("div", {"class": "tsg-rwd-qf-box-title"})

    title = []
    for i in res:
        title += [i]
    res = bs.find_all("div", {"class": "tsg-rwd-qf-box-data"})
    body = []
    for i in res:
        body += [i]
    ans = {}
    for i in range(len(title)):
        ans[title[i]] = body[i]
    return json.dumps(ans)