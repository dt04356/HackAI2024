"""
Module application
"""
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv("openai.env")
client = OpenAI()

def pullImage(str):
    response = client.images.generate(
        prompt = str,
        size = "1024x1024",
        quality="standard",
        n=1,
    )
    newjson = response.model_dump_json()
    url = parseResponse(newjson)
    
def parseResponse(response):
    url = ''
    ln = len(response)
    place = response.find('url')
    url = response[place+6:ln-4]
    return url


pullImage("a cat with a hat")
