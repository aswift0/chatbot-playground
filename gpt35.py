import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("my_key"),
)

def chatbot():
  # Create a list to store all the messages for context
  messages = [
    {"role": "system", "content": "You are a helpful assistant."},
  ]

  while True:
    message = input("User: ")

    if message.lower() == "quit":
      break

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_message = response['choices'][0]['message']['content']
    print(f"Bot: {chat_message}")
    messages.append({"role": "assistant", "content": chat_message})

if __name__ == "__main__":
  print("Start chatting with the bot (type 'quit' to stop)!")
  chatbot()