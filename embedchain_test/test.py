import os
from mytoken import apikey

from embedchain import App

os.environ["OPENAI_API_KEY"] = apikey

wikipedia_bot = App()

# Embed Online Resources

wikipedia_bot.add("https://en.wikipedia.org/wiki/Donald_Trump")
wikipedia_bot.add("https://en.wikipedia.org/wiki/Barack_Obama")

while True:
    question = input("Enter your question, or 'quit' to stop the program.\n >>")

    if question == 'quit':
        break

    response = wikipedia_bot.query(question)
    print(f"\n{response}\n")