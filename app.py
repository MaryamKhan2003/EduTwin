import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🧠 EduTwin AI")

    st.caption(
        "Personalized Learning Intelligence"
    )

    st.divider()

    st.subheader("🚀 Explore EduTwin")

    st.write(
        """
        👤 **Digital Twin**

        Build your personalized learner profile.
        """
    )

    st.write(
        """
        📷 **Vision Tutor**

        Understand diagrams, code and educational images.
        """
    )

    st.write(
        """
        📚 **Adaptive Learning**

        Learn according to your knowledge level.
        """
    )

    st.write(
        """
        💼 **Career Intelligence**

        Discover your career readiness.
        """
    )

    st.write(
        """
        🎤 **Interview Practice**

        Prepare for your target career.
        """
    )

    st.divider()

    st.info(
        """
        💡 **EduTwin Principle**

        First understand the learner.

        Then understand what they are learning.

        Finally, personalize the experience.
        """
    )

    st.divider()

    st.caption(
        "AI-Powered Personal Digital Twin"
    )


# ==================================================
# HERO
# ==================================================

st.title("🧠 EduTwin AI")

st.subheader(
    "Your Personal AI Learning Twin"
)

st.write(
    """
    ### Learn smarter. Grow faster. Build your future.

    EduTwin combines **Digital Twin technology,
    Generative AI and Vision AI** to create a
    learning experience around *you*.
    """
)

st.write("")

# Main CTA
if st.button(
    "🚀 Build My Digital Twin",
    type="primary",
    use_container_width=True
):

    st.switch_page(
        "pages/profile.py"
    )


# ==================================================
# FEATURE CARDS
# ==================================================

st.divider()

st.header(
    "✨ One AI. Your Entire Learning Journey."
)

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader(
        "👤 Know Me"
    )

    st.write(
        """
        Upload your CV or create your profile.

        EduTwin understands your education,
        skills, projects, interests and
        career goals.
        """
    )


with col2:

    st.subheader(
        "👁️ See With Me"
    )

    st.write(
        """
        Upload an educational image.

        Vision AI identifies what you're
        looking at and explains it according
        to your learning needs.
        """
    )


with col3:

    st.subheader(
        "🎯 Guide Me"
    )

    st.write(
        """
        Connect your current skills with
        your target career.

        Discover what you should learn next.
        """
    )


# ==================================================
# HOW IT WORKS
# ==================================================

st.divider()

st.header(
    "🔄 How EduTwin Works"
)

step1, step2, step3, step4 = st.columns(4)


with step1:

    st.metric(
        "01",
        "Understand"
    )

    st.caption(
        "Build your Digital Twin."
    )


with step2:

    st.metric(
        "02",
        "Learn"
    )

    st.caption(
        "Get personalized explanations."
    )


with step3:

    st.metric(
        "03",
        "Practice"
    )

    st.caption(
        "Test and improve your knowledge."
    )


with step4:

    st.metric(
        "04",
        "Grow"
    )

    st.caption(
        "Follow your career roadmap."
    )


# ==================================================
# LEARNING LOOP
# ==================================================

st.divider()

st.header(
    "🧠 The Intelligent Learning Loop"
)

st.info(
    """
    **Your Profile**
    → **Personalized Learning**
    → **Practice**
    → **Assessment**
    → **Skill Gap Detection**
    → **Recommendation**
    → **Better Learning**
    """
)


# ==================================================
# FEATURE NAVIGATION
# ==================================================

st.divider()

st.header(
    "🚀 Explore EduTwin"
)

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "📷 Open Vision Tutor",
        use_container_width=True
    ):

        st.switch_page(
            "pages/vision_tutor.py"
        )


with col2:

    if st.button(
        "💼 Explore Career Intelligence",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )


st.write("")

col1, col2 = st.columns(2)


with col1:

    if st.button(
        "📚 Start Adaptive Learning",
        use_container_width=True
    ):

        st.switch_page(
            "pages/learning.py"
        )


with col2:

    if st.button(
        "🎤 Practice Interview",
        use_container_width=True
    ):

        st.switch_page(
            "pages/interview.py"
        )


# ==================================================
# FINAL CTA
# ==================================================

st.divider()

st.header(
    "🚀 Ready to build your AI learning twin?"
)

st.write(
    """
    Your learning journey starts with understanding
    where you are today.
    """
)

if st.button(
    "🧠 Create My Digital Twin →",
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
