import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🧠 EduTwin AI")

    st.caption(
        "Your Personal AI Learning Twin"
    )

    st.divider()

    st.subheader("🚀 Quick Start")

    st.write(
        """
        **1.** Create your Digital Twin

        **2.** Explore Vision Tutor

        **3.** Learn with Adaptive AI

        **4.** Analyze your career

        **5.** Practice interviews
        """
    )

    st.divider()

    st.info(
        "💡 EduTwin adapts learning around "
        "your skills and career goals."
    )

    st.divider()

    st.caption(
        "AI-Powered Personalized Learning"
    )


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.title("🧠 EduTwin AI")

st.subheader(
    "Your Personal AI Learning Twin"
)

st.write(
    """
    **Learn smarter. Understand faster. Build your career.**

    EduTwin creates a personalized learning experience
    based on your **knowledge, skills, interests and
    career goals**.
    """
)

st.write("")


# --------------------------------------------------
# PRIMARY ACTIONS
# --------------------------------------------------

st.header("🚀 Start Your Journey")

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("👤 Digital Twin")

    st.write(
        """
        Build your personal learner profile
        using your CV, education, skills,
        projects and career goal.
        """
    )

    if st.button(
        "Build My Digital Twin →",
        use_container_width=True,
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )


with col2:

    st.subheader("📷 Vision Tutor")

    st.write(
        """
        Upload a diagram, graph, code screenshot
        or educational image and let AI explain it.
        """
    )

    if st.button(
        "Try Vision Tutor →",
        use_container_width=True
    ):

        st.switch_page(
            "pages/vision_tutor.py"
        )


with col3:

    st.subheader("💼 Career Intelligence")

    st.write(
        """
        Discover your career readiness and
        identify the skills you need to improve.
        """
    )

    if st.button(
        "Explore Careers →",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )


# --------------------------------------------------
# VALUE PROPOSITION
# --------------------------------------------------

st.divider()

st.header("✨ What Makes EduTwin Different?")

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("👤 Understand Me")

    st.write(
        """
        EduTwin builds a learner profile from
        your education, skills, courses,
        projects and career goals.
        """
    )


with col2:

    st.subheader("👁️ Understand What I See")

    st.write(
        """
        Vision AI analyzes educational images
        and explains them according to your
        current learning level.
        """
    )


with col3:

    st.subheader("🎯 Guide My Future")

    st.write(
        """
        AI connects your current abilities
        with the skills required for your
        target career.
        """
    )


# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------

st.divider()

st.header("🔄 How EduTwin Works")

step1, step2, step3, step4 = st.columns(4)


with step1:

    st.metric(
        "01",
        "Know You"
    )

    st.caption(
        "Build your Digital Twin."
    )


with step2:

    st.metric(
        "02",
        "Teach You"
    )

    st.caption(
        "Generate personalized learning."
    )


with step3:

    st.metric(
        "03",
        "Test You"
    )

    st.caption(
        "Measure your understanding."
    )


with step4:

    st.metric(
        "04",
        "Guide You"
    )

    st.caption(
        "Recommend your next step."
    )


# --------------------------------------------------
# LEARNING LOOP
# --------------------------------------------------

st.divider()

st.header("🧠 The EduTwin Learning Loop")

st.info(
    """
    **Your Profile → AI Learning → Practice → Assessment
    → Skill Gaps → Personalized Recommendations → Improved Profile**
    """
)


# --------------------------------------------------
# FINAL CTA
# --------------------------------------------------

st.divider()

st.header(
    "🚀 Ready to build your Digital Twin?"
)

st.write(
    """
    Start by uploading your CV or creating your
    learner profile manually.
    """
)

if st.button(
    "🧠 Create My Digital Twin",
    type="primary",
    use_container_width=True
):

    st.switch_page(
        "pages/profile.py"
    )


st.write("")

st.caption(
    "🧠 EduTwin AI • Personalized Learning Intelligence"
)
