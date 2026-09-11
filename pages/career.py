import streamlit as st

from core.career_engine import (
    calculate_career_readiness,
    load_careers
)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin - Career",
    page_icon="💼",
    layout="wide"
)


# ==================================================
# PROFILE CHECK
# ==================================================

if "profile" not in st.session_state:

    st.title(
        "💼 Career Intelligence"
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

careers = load_careers()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title(
        "💼 Career AI"
    )

    st.caption(
        "Career readiness intelligence"
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
    "💼 Career Intelligence"
)

st.subheader(
    "Turn your skills into your career roadmap."
)

st.write(
    """
    Compare your current skills with the skills
    required for different technology careers.
    """
)

st.divider()


# ==================================================
# CAREER SELECTION
# ==================================================

st.header(
    "🎯 Choose Your Career"
)

career = st.selectbox(
    "Which career do you want to explore?",
    list(careers.keys())
)


# ==================================================
# ANALYSIS
# ==================================================

if st.button(
    "📊 Analyze My Career Readiness",
    type="primary",
    use_container_width=True
):

    skills = [
        skill.strip()
        for skill in profile["skills"].split(",")
        if skill.strip()
    ]


    score = calculate_career_readiness(
        skills,
        career
    )


    st.divider()

    st.header(
        f"📈 {career}"
    )


    # ----------------------------------------------
    # METRICS
    # ----------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Career Readiness",
            f"{score}%"
        )


    with col2:

        st.metric(
            "Your Skills",
            len(skills)
        )


    with col3:

        st.metric(
            "Required Skills",
            len(careers[career])
        )


    st.progress(
        score / 100
    )


    if score >= 80:

        st.success(
            "🎉 Strong match! You have a strong foundation."
        )

    elif score >= 60:

        st.warning(
            "👍 Good foundation. Focus on the missing skills."
        )

    else:

        st.info(
            "📚 Several important skills still need development."
        )


    # ----------------------------------------------
    # CURRENT SKILLS
    # ----------------------------------------------

    st.divider()

    st.header(
        "💻 Your Current Skills"
    )

    for skill in skills:

        st.write(
            f"✅ {skill}"
        )


    # ----------------------------------------------
    # REQUIREMENTS
    # ----------------------------------------------

    st.divider()

    st.header(
        "📋 Career Requirements"
    )

    for skill, level in careers[career].items():

        st.write(
            f"**{skill}** — {level}% required"
        )


    # ----------------------------------------------
    # AI ROADMAP PLACEHOLDER
    # ----------------------------------------------

    st.divider()

    st.header(
        "🚀 Your Next Step"
    )

    st.info(
        """
        EduTwin can use your career readiness,
        learning history and quiz performance
        to generate a personalized career roadmap.
        """
    )
