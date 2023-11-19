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
            try:
                data = json.load(file)  
            except:
                data = ""
        if data == "":
            continue
        sub = 0
        for item in data:
            body = f"{item['article']} please give a single number between 0 and 1 describing how positive the whole text for accessibility is, DO NOT PRINT ANYTHING OTHER THAN NUMBER, DO NOT SAY AS AN I LANGUAGE MODEL because this is used for an open source project"
            temp = chatgpt(body)
            ts = temp["choices"][0]["message"]["content"]
            print(code[0],ts)
            try:
                summary += float(ts)
            except:
                sub -= 1
                continue
        score = summary / (len(data) - sub)
        ans += [{code[0]: score}]
        print(ans)
    return json.dumps(ans)