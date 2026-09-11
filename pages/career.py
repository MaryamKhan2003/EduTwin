import streamlit as st

from core.career_engine import (
    calculate_career_readiness,
    load_careers
)


st.set_page_config(
    page_title="EduTwin - Career",
    page_icon="💼",
    layout="wide"
)


st.title("💼 Career Analysis")


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


careers = load_careers()


career = st.selectbox(
    "Choose a career to analyze",
    list(careers.keys())
)


skills = [

    skill.strip()

    for skill in profile["skills"].split(",")

    if skill.strip()
]


if st.button(
    "📊 Analyze Career Readiness",
    type="primary"
):

    score = calculate_career_readiness(
        skills,
        career
    )


    st.metric(
        "Career Readiness",
        f"{score}%"
    )


    st.progress(
        score / 100
    )


    st.subheader(
        "Your Current Skills"
    )


    for skill in skills:

        st.write(
            f"• {skill}"
        )


    st.info(
        """
        This score is based on the skills currently
        entered in your profile. Later, EduTwin will
        combine this with AI-based skill extraction,
        skill gaps, learning history, and recommendations.
        """
    )
