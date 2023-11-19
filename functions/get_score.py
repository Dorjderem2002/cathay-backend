import requests
import openai
from functions.country_code import country_codes
import json

def chatgpt(input):
    api_key = '9f25143a3f90494996386c19d177fe41'
    api_key_2 = '17eb585e8fdf4e329e19b2f285a4fe8d'

    openai.api_type = "azure"
    openai.api_base = "https://team44.openai.azure.com/"
    openai.api_version = "2023-07-01-preview"
    openai.api_key = api_key
    message_text = [{"role":"system","content":input}]
    
    completion = openai.ChatCompletion.create(
        engine="nice",
        messages = message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return completion

def get_score():
    ans = []
    for code in country_codes:
        file = "data/news_text_" + code[1] + ".json"
        summary = ""
        with open(file, 'r') as file:
            data = json.load(file)
        for item in data:
            body = f"{item['article']} summarize information in 1 sentence whether article is talking good or bad about support and help for disabled people"
            ans = chatgpt(body)
            summary += ans["choices"][0]["message"]["content"]
        score = chatgpt(f"{summary}\n please give a single number between 0 and 1 describing how friendly the country is to disabled people given the cirsumstance, DO NOT PRINT ANYTHING OTHER THAN SINGLE FLOATING POINT NUMBER!")
        ans += [score["choices"][0]["message"]["content"]]
        print(score)
    return ans