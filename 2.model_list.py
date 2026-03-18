##
## Concept    : Exploring Available Models
## What it does: Fetches and prints all AI models available to your OpenAI API key.
## What you'll learn:
##   - How to use client.models.list() to discover available models
##   - The structure of the model list response (model IDs, types)
##   - Useful for knowing which models you have access to before building with them
## Run: python 2.model_list.py
##
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

model_list = client.models.list()

print(f"Total models available: {len(model_list.data)}")

for model in model_list.data:
    print(model.id)