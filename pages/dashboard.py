import streamlit as st


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EduTwin - Dashboard",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# PROFILE CHECK
# --------------------------------------------------

if "profile" not in st.session_state:

    st.title("📊 Your Dashboard")

    st.warning(
        "Your Digital Twin has not been created yet."
    )

    st.write(
        """
        Create your profile first so EduTwin can
        personalize your dashboard.
        """
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


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🧠 EduTwin AI")

    st.caption(
        "Learning Dashboard"
    )

    st.divider()

    st.write(
        f"👋 **{profile['name']}**"
    )

    st.write(
        f"🎯 {profile['career_goal']}"
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title(
    "📊 Your Digital Twin"
)

st.subheader(
    f"Welcome back, {profile['name']} 👋"
)

st.write(
    """
    Here is a snapshot of your current learning
    profile and career direction.
    """
)

st.divider()


# --------------------------------------------------
# PROFILE METRICS
# --------------------------------------------------

skills = [
    x.strip()
    for x in profile["skills"].split(",")
    if x.strip()
]

courses = [
    x.strip()
    for x in profile["courses"].split(",")
    if x.strip()
]

projects = [
    x.strip()
    for x in profile["projects"].split(",")
    if x.strip()
]


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "💻 Skills",
        len(skills)
    )


with col2:

    st.metric(
        "📚 Courses",
        len(courses)
    )


with col3:

    st.metric(
        "🚀 Projects",
        len(projects)
    )


with col4:

    st.metric(
        "🎯 Career",
        profile["career_goal"]
    )


# --------------------------------------------------
# PROFILE OVERVIEW
# --------------------------------------------------

st.divider()

st.header(
    "👤 Profile Overview"
)

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "🎓 Education"
    )

    st.info(
        profile["education"]
    )

    st.subheader(
        "💻 Skills"
    )

    for skill in skills:

        st.write(
            f"✅ {skill}"
        )


with col2:

    st.subheader(
        "🎯 Career Goal"
    )

    st.success(
        profile["career_goal"]
    )

    st.subheader(
        "💡 Interests"
    )

    if profile["interests"].strip():

        st.write(
            profile["interests"]
        )

    else:

        st.caption(
            "No interests added yet."
        )


# --------------------------------------------------
# COURSES AND PROJECTS
# --------------------------------------------------

st.divider()

col1, col2 = st.columns(2)


with col1:

    st.header(
        "📚 Courses"
    )

    if courses:

        for course in courses:

            st.write(
                f"📘 {course}"
            )

    else:

        st.caption(
            "No courses added yet."
        )


with col2:

    st.header(
        "🚀 Projects"
    )

    if projects:

        for project in projects:

            st.write(
                f"🔹 {project}"
            )

    else:

        st.caption(
            "No projects added yet."
        )


# --------------------------------------------------
# QUICK ACTIONS
# --------------------------------------------------

st.divider()

st.header(
    "⚡ Continue Learning"
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    if st.button(
        "📷 Vision Tutor",
        use_container_width=True
    ):

        st.switch_page(
            "pages/vision_tutor.py"
        )


with col2:

    if st.button(
        "📚 Learn",
        use_container_width=True
    ):

        st.switch_page(
            "pages/learning.py"
        )


with col3:

    if st.button(
        "💼 Career",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )


with col4:

    if st.button(
        "🎤 Interview",
        use_container_width=True
    ):

        st.switch_page(
            "pages/interview.py"
        )


# --------------------------------------------------
# DIGITAL TWIN MESSAGE
# --------------------------------------------------

st.divider()

st.info(
    """
    🧠 **Your Digital Twin is the foundation of EduTwin.**

    As you learn, practice and improve, future versions
    can update this profile with your learning progress,
    quiz performance and skill development.
    """
)
