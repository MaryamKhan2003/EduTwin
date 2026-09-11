import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🧠 EduTwin")

    st.caption(
        "AI Learning Intelligence"
    )

    st.divider()

    st.subheader(
        "Your AI Learning Companion"
    )

    st.write(
        "Build your skills, understand what you see, "
        "and move closer to your career goals."
    )

    st.divider()

    st.caption(
        "Use the navigation above to explore EduTwin."
    )


# ============================================================
# HERO SECTION
# ============================================================

st.title(
    "🧠 EduTwin AI"
)

st.subheader(
    "Your Personal AI Learning Twin"
)

st.write(
    """
    EduTwin creates a personalized learning experience
    around **your skills, knowledge, interests, and career goals**.
    """
)

st.write("")


# ============================================================
# QUICK ACTIONS
# ============================================================

st.header(
    "🚀 Start Your Journey"
)

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader(
        "👤 Digital Twin"
    )

    st.write(
        "Create your personalized learner profile "
        "with your education, skills, projects, "
        "interests and career goal."
    )

    if st.button(
        "Build My Digital Twin",
        use_container_width=True,
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )


with col2:

    st.subheader(
        "📷 Vision Tutor"
    )

    st.write(
        "Upload a diagram, graph, computer component, "
        "code screenshot or educational image."
    )

    if st.button(
        "Try Vision Tutor",
        use_container_width=True
    ):

        st.switch_page(
            "pages/vision_tutor.py"
        )


with col3:

    st.subheader(
        "💼 Career AI"
    )

    st.write(
        "Compare your current skills with the "
        "skills required for your target career."
    )

    if st.button(
        "Explore Careers",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )


st.divider()


# ============================================================
# FEATURES
# ============================================================

st.header(
    "✨ What Can EduTwin Do?"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader(
        "👤 Understand Me"
    )

    st.write(
        """
        EduTwin builds a learner profile using your
        education, skills, courses, projects,
        interests and career goals.
        """
    )


with col2:

    st.subheader(
        "📷 Understand What I See"
    )

    st.write(
        """
        Show EduTwin an educational image and
        AI can identify and explain what is visible.
        """
    )


with col3:

    st.subheader(
        "🎯 Guide My Future"
    )

    st.write(
        """
        Analyze your career readiness and discover
        which skills you should improve.
        """
    )


st.divider()


# ============================================================
# HOW IT WORKS
# ============================================================

st.header(
    "🔄 How EduTwin Works"
)


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
        "Create personalized learning."
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
        "Improve your next learning step."
    )


st.divider()


# ============================================================
# DIFFERENTIATOR
# ============================================================

st.header(
    "✨ What Makes EduTwin Different?"
)

st.info(
    """
    Traditional learning gives everyone the same content.

    **EduTwin first understands the learner, then understands
    what they are learning, and finally adapts the experience
    around their knowledge and career goal.**
    """
)


st.write("")


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "🧠 EduTwin AI • Personalized Learning Intelligence"
)
