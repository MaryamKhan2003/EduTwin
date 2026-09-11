import streamlit as st

from core.career_engine import (
    calculate_career_readiness,
    get_skill_gaps,
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


st.divider()


if st.button(
    "📊 Analyze Career Readiness",
    type="primary"
):

    score = calculate_career_readiness(
        skills,
        career
    )

    gaps = get_skill_gaps(
        skills,
        career
    )


    st.subheader(
        "Career Readiness"
    )


    st.metric(
        "Readiness Score",
        f"{score}%"
    )


    st.progress(
        int(score)
    )


    st.divider()


    st.subheader(
        "💻 Your Current Skills"
    )


    for skill in skills:

        st.write(
            f"• {skill}"
        )


    st.divider()


    st.subheader(
        "⚠️ Skill Gaps"
    )


    if gaps:

        for gap in gaps:

            st.write(
                f"**{gap['skill']}** — "
                f"Current: {gap['current']} | "
                f"Required: {gap['required']} | "
                f"Gap: {gap['gap']}"
            )

    else:

        st.success(
            "No major skill gaps were detected!"
        )


    st.info(
        """
        The current version calculates readiness
        from the skills entered in your Digital Twin.
        """
    )
