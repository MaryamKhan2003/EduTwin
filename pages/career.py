import streamlit as st

from core.career_engine import (
    calculate_career_readiness,
    load_careers
)

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Career",
    page_icon="💼",
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
            AI CAREER INTELLIGENCE
        </div>

        <div class="hero-title">
            Discover your career readiness. 💼
        </div>

        <div class="hero-text">
            Compare your current skills with the skills
            required for different technology careers.
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
# CAREER DATA
# =========================================

careers = load_careers()


st.markdown(
    '<div class="section-label">CAREER ANALYSIS</div>',
    unsafe_allow_html=True
)

st.subheader(
    "🎯 Choose a career"
)


career = st.selectbox(
    "Career",
    list(careers.keys())
)


skills = [
    skill.strip()
    for skill in profile["skills"].split(",")
    if skill.strip()
]


# =========================================
# ANALYZE
# =========================================

if st.button(
    "📊 Analyze My Career Readiness",
    type="primary"
):

    score = calculate_career_readiness(
        skills,
        career
    )


    st.write("")


    # =====================================
    # SCORE
    # =====================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="font-size:30px;">
                    🎯
                </div>

                <div class="stat-number">
                    {score}%
                </div>

                <div class="stat-label">
                    Career Readiness
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="font-size:30px;">
                    💻
                </div>

                <div class="stat-number">
                    {len(skills)}
                </div>

                <div class="stat-label">
                    Your Skills
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        required_count = len(
            careers[career]
        )

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="font-size:30px;">
                    📋
                </div>

                <div class="stat-number">
                    {required_count}
                </div>

                <div class="stat-label">
                    Required Skills
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    st.subheader(
        f"📈 {career} Readiness"
    )


    st.progress(
        score / 100
    )


    # =====================================
    # CURRENT SKILLS
    # =====================================

    st.markdown(
        '<div class="section-label">YOUR STRENGTHS</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        "💪 Current Skills"
    )


    if skills:

        for skill in skills:

            st.success(
                f"✓ {skill}"
            )

    else:

        st.info(
            "No skills found in your profile."
        )


    # =====================================
    # REQUIRED SKILLS
    # =====================================

    st.markdown(
        '<div class="section-label">CAREER REQUIREMENTS</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        f"📋 Skills commonly required for {career}"
    )


    for skill, level in careers[career].items():

        st.write(
            f"**{skill}** — {level}%"
        )


    st.info(
        """
        This readiness score is based on the skills
        currently entered in your Digital Twin.

        Future versions can combine this score with
        AI skill extraction, quiz performance,
        learning history and personalized recommendations.
        """
    )
