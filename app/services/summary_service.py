import openai
import requests
from bs4 import BeautifulSoup
from decouple import config
from gensim.summarization.summarizer import summarize

from app.models.response_model import response_model_from_dict
from config.constants import *

def extract_text(url, api_key):
    headers = {'apiKey': api_key}
    page = requests.get(url, headers=headers)
    page.raise_for_status()
    soup = BeautifulSoup(page.text, "html.parser")
    return soup.text


def summarize_text(text):
    summary = text
    while True:
        if(len(summary.split()) > 500):
            summary = summarize(summary, ratio=0.5, word_count=500)
            if summary == '':
                print("Summarization could not reduce the text to less than 500 words.")
                break
        break;
    return summary


def get_gpt3_summary(summary, isPoints):
    if isPoints:
        prompt = PROMPT_FOR_POINTS.format(summary)
        print('//////////////\nPROMPT: {0}'.format(prompt))
        response = openai.Completion.create(engine=ENGINE, max_tokens=MAX_TOKENS, n=1, stop=None,
                                            temperature=TEMPERATURE, prompt=prompt)
    else:
        prompt = PROMPT_FOR_SUMMARY.format(summary)
        print('//////////////\nPROMPT: {0}'.format(prompt))
        response = openai.Completion.create(engine=ENGINE, max_tokens=MAX_TOKENS, n=1, stop=None,
                                            temperature=TEMPERATURE, prompt=prompt)
    print(response)
    responseModel = response_model_from_dict(response)
    return responseModel.choices[0].text

def get_website_summary(url, isPoints, api_key):
    text = extract_text(url, api_key)
    summary = summarize_text(text)
    print('Key={0}'.format(api_key))
    return 'Summary:\n {0}'.format(summary)
    return get_gpt3_summary(summary, isPoints)