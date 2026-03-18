##
## Concept    : First OpenAI API Call — Chat Completions
## What it does: Sends a simple chat request to the OpenAI API and prints the response.
##               Uses a system message to set the assistant's role (English-to-Hindi translator)
##               and a user message with the text to translate.
## What you'll learn:
##   - How to authenticate with the OpenAI API using an API key from a .env file
##   - The structure of the messages list: system role vs user role
##   - How to call client.chat.completions.create() and read the response
##   - The difference between the model parameter and the messages parameter
## Run: python 1.hello_world.py
##
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

messages = [
    {"role" : "system", "content" : "You are a helpful assistant that translates English to Hindi."},
    {"role" : "user", "content" : "Translate the following English text to Hindi: 'Hello, how are you?'"}
]

model="gpt-4.1-mini"

completion = client.chat.completions.create(
    model=model,
    messages=messages
)

print(completion.choices[0].message.content)