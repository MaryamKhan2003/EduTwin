import streamlit as st
from groq import Groq


TEXT_MODEL = "qwen/qwen3.6-27b"
VISION_MODEL = "qwen/qwen3.6-27b"


def get_groq_client():

    if "GROQ_API_KEY" not in st.secrets:
        raise ValueError(
            "GROQ_API_KEY is not configured in Streamlit Secrets."
        )

    return Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )


def ask_groq(prompt, model=TEXT_MODEL):

    client = get_groq_client()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_completion_tokens=900
    )

    return response.choices[0].message.content
