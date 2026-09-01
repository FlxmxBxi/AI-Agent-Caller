from openai import OpenAI
import streamlit as s
s.set_page_config(page_title="Damians's AI", page_icon="🚀")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = s.secrets["API_KEY"],
)
#secondary code if you have one "API KEY"


def chat(history):
    

    
    stream = client.chat.completions.create(
        model="x-ai/grok-build-0.1",
        messages=history,
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content
