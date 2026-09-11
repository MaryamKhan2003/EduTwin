import streamlit as st

from ai.groq_client import ask_groq
from ai.prompts import build_learning_prompt


st.set_page_config(
    page_title="EduTwin - Learning",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "📚 Adaptive Learning"
)

st.subheader(
    "Learn something that matters."
)

st.write(
    """
    EduTwin creates a learning explanation based on
    your knowledge, skills and career goal.
    """
)

st.divider()


# ============================================================
# PROFILE CHECK
# ============================================================

if "profile" not in st.session_state:

    st.warning(
        "Please create your Digital Twin profile first."
    )

    if st.button(
        "👤 Create My Profile",
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )

    st.stop()


profile = st.session_state["profile"]


# ============================================================
# TOPIC
# ============================================================

st.header(
    "🧠 What do you want to learn?"
)


topic = st.text_input(
    "Learning Topic",
    placeholder="Example: Neural Networks"
)


if st.button(
    "📖 Start Personalized Learning",
    type="primary"
):

    if topic.strip() == "":

        st.warning(
            "Please enter a topic first."
        )

    else:

        try:

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            prompt = build_learning_prompt(
                topic,
                profile
            )


            with st.spinner(
                "🧠 EduTwin is preparing your lesson..."
            ):

                lesson = ask_groq(
                    prompt
                )


            st.success(
                "✅ Your personalized lesson is ready!"
            )


            st.divider()


            st.header(
                f"📚 {topic}"
            )


            st.markdown(
                lesson
            )


        except Exception as error:

            st.error(
                f"Learning AI error: {error}"
            )
