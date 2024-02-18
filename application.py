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
    return url

def pullInt():
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= [{"role":"user", "content":"give me a random integer between 0 and 10000"}]

    )
    dump =  response.model_dump_json()
    num = parseInt(dump)
    return num


def parseInt(dump):
    inte = ''
    place  = dump.find('content')
    dump = dump[place+9:len(dump)]
    pl2 = dump.find(',')
    inte = dump[0:pl2]
    num = eval(inte)
    return num

def parseResponse(response):
    url = ''
    ln = len(response)
    place = response.find('url')
    url = response[place+6:ln-4]
    return url

pullInt()

