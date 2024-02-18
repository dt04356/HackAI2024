"""
Module application
"""
import json
import os
from openai import OpenAI

client = OpenAI()

def pullImage(str):
    response = client.images.generate(
        model = "dalle-e-3",
        prompt = str,
        size = "1024x1024",
        quality="standard",
        n=1,
    )
    print(response["data"][0]["url"])

pullImage("a cat with a hat")
