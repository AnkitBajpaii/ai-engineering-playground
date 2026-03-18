##
## Concept    : Multi-Turn Conversations & Token Tracking
## What it does: An interactive programming help chatbot that remembers the full conversation
##               history across multiple turns and tracks cumulative token usage.
## What you'll learn:
##   - Why conversation history matters: the API is stateless, so you must send all
##     previous messages on every request to give the model context
##   - How to grow the messages list by appending both user and assistant messages each turn
##   - How token usage accumulates over a long conversation (important for cost awareness)
##   - The role of the system message in shaping the assistant's personality/scope
## Run: python 5.multi_turn_chatbot.py
##
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

messages=[
    {"role": "system", "content": "You are a programming expert. Answer questions about programming languages. Keep responses short, concise and to the point."}
]

over_all_usage_tokens = 0

print("Welcome to the Programming Help chatbot. Ask me a question!")
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit", "bye", "tata"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    user_message = {"role": "user", "content": user_question}

    messages.append(user_message)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
    )

    curr_tokens = response.usage.total_tokens
    over_all_usage_tokens += curr_tokens
    
    assistant_reply = response.choices[0].message.content.strip()

    print("Chat Assistant: ", assistant_reply, "\n")
    print("Token use for this interaction: ", curr_tokens, "\n")

    assistant_message = {"role":"assistant", "content": assistant_reply}

    messages.append(assistant_message)

    

print(f"Overall usage tokens: {over_all_usage_tokens}")
