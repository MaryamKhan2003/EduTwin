import streamlit as st

from ai.groq_client import ask_groq
from ai.prompts import build_learning_prompt
from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Learning",
    page_icon="📚",
    layout="wide"
)


load_css()


# =========================================
# HERO
# =========================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-small">
            PERSONALIZED AI LEARNING
        </div>

        <div class="hero-title">
            Learn something that matters. 📚
        </div>

        <div class="hero-text">
            EduTwin creates learning explanations based
            on your knowledge, skills and career goal.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# PROFILE CHECK
# =========================================

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


# =========================================
# LEARNING
# =========================================

st.markdown(
    '<div class="section-label">CHOOSE A TOPIC</div>',
    unsafe_allow_html=True
)

st.subheader(
    "🧠 What do you want to learn?"
)


topic = st.text_input(
    "Learning topic",
    placeholder=(
        "Example: Neural Networks"
    )
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


            st.markdown(
                '<div class="section-label">YOUR LESSON</div>',
                unsafe_allow_html=True
            )

            st.subheader(
                f"📚 {topic}"
            )


            st.markdown(
                lesson
            )


        except Exception as error:

            st.error(
                f"Learning AI error: {error}"
            )
