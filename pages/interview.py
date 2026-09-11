import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin - Interview",
    page_icon="🎤",
    layout="wide"
)


# ==================================================
# PROFILE CHECK
# ==================================================

if "profile" not in st.session_state:

    st.title(
        "🎤 AI Interview Practice"
    )

    st.warning(
        "Create your Digital Twin first."
    )

    if st.button(
        "👤 Create My Digital Twin",
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )

    st.stop()


profile = st.session_state["profile"]


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title(
        "🎤 Interview AI"
    )

    st.caption(
        "Practice for your future career"
    )

    st.divider()

    st.write(
        f"👤 **{profile['name']}**"
    )

    st.write(
        f"🎯 {profile['career_goal']}"
    )


# ==================================================
# HEADER
# ==================================================

st.title(
    "🎤 AI Interview Practice"
)

st.subheader(
    "Practice like it's real."
)

st.write(
    """
    Prepare for your target career with
    realistic interview questions.
    """
)

st.divider()


# ==================================================
# TARGET
# ==================================================

st.header(
    "🎯 Interview Target"
)

st.success(
    f"Target career: **{profile['career_goal']}**"
)


# ==================================================
# QUESTION
# ==================================================

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


# ==================================================
# ANSWER
# ==================================================

st.header(
    "💬 Your Answer"
)

answer = st.text_area(
    "Write your answer",
    placeholder=(
        "Answer as if you were sitting "
        "in a real interview..."
    ),
    height=180
)


# ==================================================
# EVALUATION
# ==================================================

if st.button(
    "🎯 Evaluate My Answer",
    type="primary",
    use_container_width=True
):

    if answer.strip() == "":

        st.warning(
            "Please enter your answer first."
        )

    else:

        st.success(
            "✅ Answer received!"
        )

        st.divider()

        st.header(
            "🧠 Interview Evaluation"
        )

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Communication",
                "Ready for AI"
            )


        with col2:

            st.metric(
                "Career",
                profile["career_goal"]
            )


        with col3:

            st.metric(
                "Status",
                "Practice"
            )


        st.info(
            """
            The AI interview engine can evaluate
            your answer for:

            • Technical knowledge  
            • Communication  
            • Relevance  
            • Confidence  
            • Strengths  
            • Areas for improvement
            """
        )
