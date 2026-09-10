import streamlit as st
from groq import Groq


st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 EduTwin AI")

st.write("Testing Groq AI...")


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


if st.button("Test Groq AI"):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": "Explain AI in very simple words."
            }
        ]
    )

    answer = response.choices[0].message.content

    st.write(answer)
