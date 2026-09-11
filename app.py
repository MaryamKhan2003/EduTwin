import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide"
)


load_css()


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px 5px 25px 5px;
        ">
            <div style="font-size:42px;">🧠</div>

            <div style="
                font-size:24px;
                font-weight:800;
                color:white;
            ">
                EduTwin
            </div>

            <div style="
                color:#94a3b8;
                font-size:12px;
            ">
                AI Learning Intelligence
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("YOUR LEARNING")

    st.write("👤 Digital Twin")
    st.write("📚 Adaptive Learning")
    st.write("📷 Vision Tutor")

    st.caption("YOUR CAREER")

    st.write("💼 Career Analysis")
    st.write("🎤 Interview Practice")


# ==========================================
# HERO
# ==========================================

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


# ==========================================
# BUTTONS
# ==========================================

col1, col2, col3 = st.columns(
    [1.2, 1, 1]
)


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


# ==========================================
# FEATURES
# ==========================================

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
                skills, education, projects, interests
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
                Show EduTwin a diagram, computer component,
                graph or educational image and let AI
                explain what you see.
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
                Learn topics based on your current knowledge,
                career goals and learning progress.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# HOW IT WORKS
# ==========================================

st.write("")
st.write("")

st.markdown(
    '<div class="section-label">HOW IT WORKS</div>',
    unsafe_allow_html=True
)

st.header(
    "Your learning journey becomes intelligent."
)


col1, col2, col3, col4 = st.columns(4)


steps = [
    ("01", "👤", "Know You", "Build your Digital Twin."),
    ("02", "📚", "Teach You", "Generate personalized learning."),
    ("03", "📝", "Test You", "Measure your understanding."),
    ("04", "🎯", "Guide You", "Improve your next learning step.")
]


for column, step in zip(
    [col1, col2, col3, col4],
    steps
):

    with column:

        number, icon, title, text = step

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="
                    color:#818cf8;
                    font-size:12px;
                    font-weight:700;
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
                    {text}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# INSIGHT
# ==========================================

st.markdown(
    """
    <div class="insight-card">

        <div class="insight-title">
            ✨ The idea behind EduTwin
        </div>

        <p class="insight-text">
            Traditional learning gives everyone the same content.
            EduTwin first understands the learner, then understands
            what they are learning, and finally adapts the experience
            around their knowledge and career goal.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
        🧠 EduTwin AI &nbsp;•&nbsp;
        Personalized Learning Intelligence
    </div>
    """,
    unsafe_allow_html=True
)
