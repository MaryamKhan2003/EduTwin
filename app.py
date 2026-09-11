import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide"
)


load_css()


# =========================================
# SIDEBAR BRANDING
# =========================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:20px 5px 25px 5px;
        ">

            <div style="
                font-size:44px;
                margin-bottom:5px;
            ">
                🧠
            </div>

            <div style="
                font-size:25px;
                font-weight:800;
                color:white;
            ">
                EduTwin
            </div>

            <div style="
                color:#94a3b8;
                font-size:12px;
                margin-top:5px;
            ">
                AI Learning Intelligence
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.caption(
        "YOUR AI LEARNING COMPANION"
    )

    st.write(
        "Build your skills. "
        "Understand what you see. "
        "Reach your career goals."
    )


# =========================================
# HERO
# =========================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-small">
            🧠 AI-POWERED PERSONAL LEARNING TWIN
        </div>

        <div class="hero-title">
            Learn smarter.<br>
            Grow faster.
        </div>

        <div class="hero-text">
            EduTwin understands your skills, learning needs,
            interests and career goals — then creates a
            personalized learning experience around you.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# QUICK ACTIONS
# =========================================

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "🚀 Build My Digital Twin",
        type="primary",
        use_container_width=True
    ):

        st.switch_page(
            "pages/profile.py"
        )


with col2:

    if st.button(
        "📷 Try Vision Tutor",
        use_container_width=True
    ):

        st.switch_page(
            "pages/vision_tutor.py"
        )


with col3:

    if st.button(
        "💼 Explore Careers",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )


st.write("")


# =========================================
# FEATURES
# =========================================

st.markdown(
    '<div class="section-label">THE EDUTWIN EXPERIENCE</div>',
    unsafe_allow_html=True
)

st.header(
    "One AI. Personalized around you."
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                👤
            </div>

            <div class="feature-title">
                Digital Twin
            </div>

            <div class="feature-text">
                Build an intelligent profile of your
                education, skills, projects, interests
                and career goals.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                📷
            </div>

            <div class="feature-title">
                Vision Tutor
            </div>

            <div class="feature-text">
                Show EduTwin a diagram, graph, computer
                component or educational image and let
                AI explain what you see.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">
                🧠
            </div>

            <div class="feature-title">
                Adaptive AI
            </div>

            <div class="feature-text">
                Learn topics based on your current
                knowledge, career goals and learning
                progress.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================
# HOW IT WORKS
# =========================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-label">HOW EDUTWIN WORKS</div>',
    unsafe_allow_html=True
)

st.header(
    "Your learning journey becomes intelligent."
)


col1, col2, col3, col4 = st.columns(4)


steps = [
    (
        "01",
        "👤",
        "Know You",
        "Build your Digital Twin."
    ),
    (
        "02",
        "📚",
        "Teach You",
        "Create personalized learning."
    ),
    (
        "03",
        "📝",
        "Test You",
        "Measure your understanding."
    ),
    (
        "04",
        "🎯",
        "Guide You",
        "Improve your next learning step."
    )
]


for column, step in zip(
    [col1, col2, col3, col4],
    steps
):

    number, icon, title, description = step

    with column:

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="
                    color:#818cf8;
                    font-size:12px;
                    font-weight:800;
                ">
                    {number}
                </div>

                <div style="
                    font-size:30px;
                    margin:10px;
                ">
                    {icon}
                </div>

                <div style="
                    color:white;
                    font-size:17px;
                    font-weight:700;
                ">
                    {title}
                </div>

                <div style="
                    color:#94a3b8;
                    font-size:13px;
                    margin-top:8px;
                ">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================
# MAIN IDEA
# =========================================

st.markdown(
    """
    <div class="insight-card">

        <div class="insight-title">
            ✨ What makes EduTwin different?
        </div>

        <div class="insight-text">
            Traditional learning gives everyone the same content.
            EduTwin first understands the learner, then understands
            what they are learning, and finally adapts the experience
            around their knowledge and career goal.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# FOOTER
# =========================================

st.markdown(
    """
    <div class="footer">
        🧠 EduTwin AI
        &nbsp;•&nbsp;
        Personalized Learning Intelligence
    </div>
    """,
    unsafe_allow_html=True
)
