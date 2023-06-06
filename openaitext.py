import os
import openai
from config import apikey


# you can get this code from the openai playground
openai.api_key = apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="What is the capital of india",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

