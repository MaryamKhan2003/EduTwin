import streamlit as st


st.set_page_config(
    page_title="EduTwin - Interview",
    page_icon="🎤",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "🎤 AI Interview Practice"
)

st.subheader(
    "Practice like it's real."
)

st.write(
    """
    Prepare for interviews using questions related
    to your target career.
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
# CAREER
# ============================================================

st.header(
    "🎯 Interview Target"
)


st.info(
    f"Target career: **{profile['career_goal']}**"
)


# ============================================================
# QUESTION
# ============================================================

st.header(
    "❓ Interview Question"
)


question = st.text_area(
    "Question",
    value=(
        f"Why do you want to become a "
        f"{profile['career_goal']}?"
    ),
    height=100
)


# ============================================================
# ANSWER
# ============================================================

st.header(
    "💬 Your Answer"
)


answer = st.text_area(
    "Answer",
    placeholder=(
        "Write your answer here..."
    ),
    height=200
)


# ============================================================
# EVALUATE
# ============================================================

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
            AI interview evaluation can now be connected
            to the interview engine.
            """
        )
