from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # load the environment variables from the .env file
api_key = os.getenv("OPENAI_API_KEY")
#print(api_key)

client = OpenAI()
response =client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": "Hello, how are you?"}])
#print(response)
print(response.choices[0].message.content)
# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": "Hello, how are you?"}]
# )

# print(response.choices[0].message.content)
