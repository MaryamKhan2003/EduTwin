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


# ============================================================
# HEADER
# ============================================================

st.title(
    "💼 Career Intelligence"
)

st.subheader(
    "Discover your career readiness."
)

st.write(
    """
    Compare your current skills with the skills
    required for different technology careers.
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
# CAREER DATA
# ============================================================

careers = load_careers()


skills = [
    skill.strip()
    for skill in profile["skills"].split(",")
    if skill.strip()
]


# ============================================================
# CAREER SELECTION
# ============================================================

st.header(
    "🎯 Choose a Career"
)


career = st.selectbox(
    "Select a career to analyze",
    list(careers.keys())
)


if st.button(
    "📊 Analyze My Career Readiness",
    type="primary"
):

    score = calculate_career_readiness(
        skills,
        career
    )


    st.divider()


    # ========================================================
    # SCORE
    # ========================================================

    st.header(
        f"📈 {career} Readiness"
    )


    st.metric(
        "Career Readiness",
        f"{score}%"
    )


    st.progress(
        score / 100
    )


    if score >= 80:

        st.success(
            "🎉 You have a strong skill match for this career."
        )

    elif score >= 60:

        st.warning(
            "👍 You have a good foundation, but some skills need improvement."
        )

    else:

        st.info(
            "📚 You have several important skills to develop for this career."
        )


    st.divider()


    # ========================================================
    # CURRENT SKILLS
    # ========================================================

    st.header(
        "💻 Your Current Skills"
    )


    if skills:

        for skill in skills:

            st.write(
                f"✅ {skill}"
            )

    else:

        st.info(
            "No skills found in your profile."
        )


    st.divider()


    # ========================================================
    # REQUIRED SKILLS
    # ========================================================

    st.header(
        "📋 Career Skill Requirements"
    )


    for skill, level in careers[career].items():

        st.write(
            f"**{skill}** — {level}% required"
        )


    st.info(
        """
        The current score is based on the skills
        entered in your Digital Twin.

        Future versions can combine this with
        AI skill extraction, quiz performance,
        learning history and recommendations.
        """
    )
