import requests 
import time
from newsplease import NewsPlease
import json

def scrape_urls_version_2(urls, c):
    f = open('data/news_text_' + c + ".json", 'a')
    res = []
    counter = 0
    for url in urls:
        counter += 1
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                article = NewsPlease.from_html(response.text, url)
                res.append({"title": article.title ,"article": article.maintext})
                print(c, counter, article.title)
        except requests.exceptions.Timeout:
            print(f"Skipping URL '{url}' due to timeout")
            continue
        except Exception as e:
            print(f"Error processing URL '{url}': {str(e)}")
            continue
    json.dump(res, f)
    

subscription_key = "c4ca97af53ae47f9a0f05f3cbd92495b"
endpoint = "https://api.bing.microsoft.com/v7.0/search"

# Query term(s) to search for. 
search_terms = [
    "accessible travel",
    "disability-friendly travel",
    "inclusive travel experiences",
    "barrier-free tourism",
    "accessible transportation options",
    "travel for people with disabilities",
    "disability accommodations",
    "universal design in tourism",
    "accessible hotels and accommodations",
    "traveling with mobility aids"
]

country_codes = [
    # ('Argentina', 'AR'),
    # ('Australia', 'AU'),
    # ('Austria', 'AT'),
    ('Belgium', 'BE'),
    ('Brazil', 'BR'),
    ('Canada', 'CA'),
    ('Chile', 'CL'),
    ('Denmark', 'DK'),
    ('Finland', 'FI'),
    ('France', 'FR'),
    ('Germany', 'DE'),
    ('Hong Kong SAR', 'HK'),
    ('India', 'IN'),
    ('Indonesia', 'ID'),
    ('Italy', 'IT'),
    ('Japan', 'JP'),
    ('Korea', 'KR'),
    ('Malaysia', 'MY'),
    ('Mexico', 'MX'),
    ('Netherlands', 'NL'),
    ('New Zealand', 'NZ'),
    ('Norway', 'NO'),
    ("People's Republic of China", 'CN'),
    ('Poland', 'PL'),
    ('Portugal', 'PT'),
    ('Republic of the Philippines', 'PH'),
    ('Russia', 'RU'),
    ('Saudi Arabia', 'SA'),
    ('South Africa', 'ZA'),
    ('Spain', 'ES'),
    ('Sweden', 'SE'),
    ('Switzerland', 'CH'),
    ('Taiwan', 'TW'),
    ('Turkey', 'TR'),
    ('United Kingdom', 'GB'),
    ('United States', 'US')
]

for c in country_codes:
    urls = []
    track = {}
    for term in search_terms:
        headers = {"Ocp-Apim-Subscription-Key": subscription_key, "Accept-Language": "en-gb"}
        params = {"q": term, "textDecorations": True, "textFormat": "HTML", "cc": c[1], "mkt": c[1], "count": 10}
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        for res in search_results["webPages"]["value"]:
            if res["url"] in track:
                continue
            else:
                track[res["url"]] = 1
            urls += [res["url"]]
    scrape_urls_version_2(urls, c[1])