import streamlit as st
from groq import Groq


TEXT_MODEL = "qwen/qwen3.6-27b"
VISION_MODEL = "qwen/qwen3.6-27b"


def get_groq_client():

    if "GROQ_API_KEY" not in st.secrets:

        raise ValueError(
            "GROQ_API_KEY is missing from Streamlit Secrets."
        )

    api_key = st.secrets["GROQ_API_KEY"]

    return Groq(
        api_key=api_key
    )


def ask_groq(prompt):

    client = get_groq_client()

    response = client.chat.completions.create(
        model=TEXT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_completion_tokens=2000
    )

    return response.choices[0].message.content
