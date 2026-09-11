import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Dashboard",
    page_icon="📊",
    layout="wide"
)


load_css()


st.title("📊 Your Digital Twin")


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


skills = [
    item.strip()
    for item in profile["skills"].split(",")
    if item.strip()
]


courses = [
    item.strip()
    for item in profile["courses"].split(",")
    if item.strip()
]


st.markdown(
    f"""
    <div class="hero">

        <div class="hero-small">
            YOUR DIGITAL TWIN
        </div>

        <div class="hero-title">
            Welcome back, {profile["name"]} 👋
        </div>

        <div class="hero-text">
            Target career: <b>{profile["career_goal"]}</b>
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# STATS
# ==========================================

col1, col2, col3, col4 = st.columns(4)


stats = [
    ("👤", profile["career_goal"], "Career Goal"),
    ("💻", str(len(skills)), "Skills"),
    ("📚", str(len(courses)), "Courses"),
    ("🧠", "Active", "Twin Status")
]


for column, stat in zip(
    [col1, col2, col3, col4],
    stats
):

    with column:

        icon, value, label = stat

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


# ==========================================
# DIGITAL TWIN
# ==========================================

st.markdown(
    '<div class="section-label">YOUR PROFILE</div>',
    unsafe_allow_html=True
)

st.header("🧠 Digital Twin Overview")


col1, col2 = st.columns(2)


with col1:

    st.markdown(
        f"""
        <div class="feature-card">

            <div class="feature-title">
                🎯 Career Direction
            </div>

            <div class="feature-text">

                <b>Target Career</b><br>
                {profile["career_goal"]}

                <br><br>

                <b>Education</b><br>
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

            <div class="feature-title">
                💻 Skills
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

            <div class="feature-title">
                🚀 Projects
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

            <div class="feature-title">
                🎯 Interests
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


# ==========================================
# QUICK ACTIONS
# ==========================================

st.markdown(
    '<div class="section-label">QUICK ACTIONS</div>',
    unsafe_allow_html=True
)

st.header("⚡ What do you want to do?")


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
