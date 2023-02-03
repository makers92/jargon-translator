import os
import sys
from fastapi import FastAPI
import openai

app=FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")
print(os.getenv("OPENAI_API_KEY"))

def get_answer(phrase):
  prompt=f"""
  Please translate the following phrase into the corporate jargon of a McKinsey consultant: {phrase}
  """

  completion = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=150,
    top_p=0.25,
    frequency_penalty=1,
    presence_penalty=1,
  )
  return completion.choices[0].text

@app.get("/corporateJargon/{phrase}")
async def translate_phrase(phrase):
    return {"translation": get_answer(phrase)}
