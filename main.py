import os
import sys
from fastapi import FastAPI
import openai
#importing packages

app=FastAPI()
#calling FastAPI

openai.api_key = os.getenv("OPENAI_API_KEY")
print(os.getenv("OPENAI_API_KEY"))
#retrieving the API key

def get_answer(phrase):
  #defining our function & its parameters
  prompt=f"""
  Translate the following phrase into corporate jargon: {phrase}
  """
  completion = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=150,
    top_p=0.25,
    frequency_penalty=1,
    presence_penalty=1,
    #request body for completions endpoint
  )
  return completion.choices[0].text
#returns the API result in text

@app.get("/corporateJargon/{phrase}")
async def translate_phrase(phrase):
    return {"translation": get_answer(phrase)}
#returns our get_answer function to FastAPI
