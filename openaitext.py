import os
import openai
from config import apikey
import random 

def ai(prompt):
  # you can get this code from the openai playground
  openai.api_key = apikey

  text = f"OpenAI response for Prompt : {prompt} \n ***********************\n"

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  try:
    text += response["choices"][0]["text"]
    # print(text)

    if not os.path.exists("Openai"):
      os.mkdir("Openai")
    
    with open (f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
      f.write(text)

  except Exception as e:
    print("Error occured !", e)
 