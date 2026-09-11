import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Interview",
    page_icon="🎤",
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
            AI CAREER COACH
        </div>

        <div class="hero-title">
            Practice like it's real. 🎤
        </div>

        <div class="hero-text">
            Prepare for interviews using questions
            related to your target career.
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
# INTERVIEW
# =========================================

st.markdown(
    '<div class="section-label">INTERVIEW PRACTICE</div>',
    unsafe_allow_html=True
)

st.subheader(
    f"🎯 Target Career: {profile['career_goal']}"
)


question = st.text_area(
    "Interview Question",
    value=(
        f"Why do you want to become a "
        f"{profile['career_goal']}?"
    ),
    height=100
)


answer = st.text_area(
    "Your Answer",
    placeholder=(
        "Write your answer here..."
    ),
    height=200
)


if st.button(
    "🎯 Evaluate My Answer",
    type="primary"
):

    if answer.strip() == "":

        st.warning(
            "Please enter your answer first."
        )

    else:

        st.success(
            "✅ Answer received!"
        )

        st.info(
            """
            AI interview evaluation is ready
            to be connected to your interview engine.
            """
        )
