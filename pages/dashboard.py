import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Dashboard",
    page_icon="📊",
    layout="wide"
)


load_css()


st.markdown(
    """
    <div class="hero">

        <div class="hero-small">
            YOUR PERSONAL AI LEARNING SPACE
        </div>

        <div class="hero-title">
            Your Digital Twin. 🧠
        </div>

        <div class="hero-text">
            See your skills, learning profile and career
            direction in one intelligent dashboard.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# CHECK PROFILE
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
# PREPARE DATA
# =========================================

skills = [
    skill.strip()
    for skill in profile["skills"].split(",")
    if skill.strip()
]


courses = [
    course.strip()
    for course in profile["courses"].split(",")
    if course.strip()
]


# =========================================
# WELCOME
# =========================================

st.markdown(
    f"""
    <div class="insight-card">

        <div class="insight-title">
            👋 Welcome, {profile["name"]}
        </div>

        <div class="insight-text">
            Your current target career is
            <b>{profile["career_goal"]}</b>.
            EduTwin will use this goal to personalize
            your learning journey.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


# =========================================
# STATS
# =========================================

col1, col2, col3, col4 = st.columns(4)


stats = [
    (
        "🎯",
        profile["career_goal"],
        "Career Goal"
    ),
    (
        "💻",
        str(len(skills)),
        "Skills"
    ),
    (
        "📚",
        str(len(courses)),
        "Courses"
    ),
    (
        "🧠",
        "Active",
        "Twin Status"
    )
]


for column, stat in zip(
    [col1, col2, col3, col4],
    stats
):

    icon, value, label = stat

    with column:

        st.markdown(
            f"""
            <div class="stat-card">

                <div style="font-size:25px;">
                    {icon}
                </div>

                <div class="stat-number">
                    {value}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


st.write("")
st.divider()


# =========================================
# DIGITAL TWIN INFORMATION
# =========================================

st.markdown(
    '<div class="section-label">YOUR DIGITAL TWIN</div>',
    unsafe_allow_html=True
)

st.header(
    "👤 Your Learning Profile"
)


col1, col2 = st.columns(2)


with col1:

    st.markdown(
        f"""
        <div class="feature-card">

            <div class="feature-icon">
                🎓
            </div>

            <div class="feature-title">
                Education
            </div>

            <div class="feature-text">
                {profile["education"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="feature-card">

            <div class="feature-icon">
                💻
            </div>

            <div class="feature-title">
                Skills
            </div>

            <div class="feature-text">
                {profile["skills"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


col1, col2 = st.columns(2)


with col1:

    st.markdown(
        f"""
        <div class="feature-card">

            <div class="feature-icon">
                🚀
            </div>

            <div class="feature-title">
                Projects
            </div>

            <div class="feature-text">
                {profile["projects"] or "No projects added yet."}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="feature-card">

            <div class="feature-icon">
                🎯
            </div>

            <div class="feature-title">
                Interests
            </div>

            <div class="feature-text">
                {profile["interests"] or "No interests added yet."}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")
st.divider()


# =========================================
# QUICK ACTIONS
# =========================================

st.markdown(
    '<div class="section-label">QUICK ACTIONS</div>',
    unsafe_allow_html=True
)

st.header(
    "⚡ Continue your journey"
)


col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "📷 Analyze Something",
        use_container_width=True
    ):

        st.switch_page(
            "pages/vision_tutor.py"
        )


with col2:

    if st.button(
        "📚 Start Learning",
        use_container_width=True
    ):

        st.switch_page(
            "pages/learning.py"
        )


with col3:

    if st.button(
        "💼 Check Career",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )
