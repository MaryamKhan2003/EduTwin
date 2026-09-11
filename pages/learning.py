import streamlit as st

from ai.groq_client import ask_groq
from ai.prompts import build_learning_prompt


st.set_page_config(
    page_title="EduTwin - Learning",
    page_icon="📚",
    layout="wide"
)


st.title("📚 Adaptive Learning")


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


st.write(
    f"Personalized learning for **{profile['name']}**"
)


st.write(
    f"Target career: **{profile['career_goal']}**"
)


st.divider()


topic = st.text_input(
    "What do you want to learn?",
    placeholder="Example: Neural Networks"
)


if st.button(
    "🧠 Generate Personalized Lesson",
    type="primary"
):

    if topic.strip() == "":

        st.warning(
            "Please enter a topic first."
        )

    else:

        prompt = build_learning_prompt(
            topic,
            profile
        )

        try:

            with st.spinner(
                "Groq AI is creating your lesson..."
            ):

                lesson = ask_groq(
                    prompt
                )

            st.subheader(
                f"📖 {topic}"
            )

            st.markdown(
                lesson
            )

        except Exception as error:

            st.error(
                f"Learning AI error: {error}"
            )
