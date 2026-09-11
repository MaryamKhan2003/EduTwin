import streamlit as st


st.set_page_config(
    page_title="EduTwin - Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# PROFILE CHECK
# ============================================================

if "profile" not in st.session_state:

    st.title("📊 Digital Twin Dashboard")

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


# ============================================================
# HEADER
# ============================================================

st.title(
    "📊 Your Digital Twin"
)

st.subheader(
    f"Welcome, {profile['name']} 👋"
)

st.write(
    """
    This dashboard gives you a quick view of your
    current learning profile.
    """
)

st.divider()


# ============================================================
# DATA
# ============================================================

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


projects = [
    project.strip()
    for project in profile["projects"].split(",")
    if project.strip()
]


# ============================================================
# METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🎯 Career Goal",
        profile["career_goal"]
    )


with col2:

    st.metric(
        "💻 Skills",
        len(skills)
    )


with col3:

    st.metric(
        "📚 Courses",
        len(courses)
    )


with col4:

    st.metric(
        "🚀 Projects",
        len(projects)
    )


st.divider()


# ============================================================
# PROFILE
# ============================================================

st.header(
    "👤 Your Learning Profile"
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
            f"• {skill}"
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

    if profile["interests"]:

        st.write(
            profile["interests"]
        )

    else:

        st.caption(
            "No interests added yet."
        )


st.divider()


# ============================================================
# PROJECTS AND COURSES
# ============================================================

col1, col2 = st.columns(2)


with col1:

    st.header(
        "📚 Courses"
    )

    if courses:

        for course in courses:

            st.write(
                f"• {course}"
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
                f"• {project}"
            )

    else:

        st.caption(
            "No projects added yet."
        )


st.divider()


# ============================================================
# QUICK ACTIONS
# ============================================================

st.header(
    "⚡ Continue Learning"
)


col1, col2, col3 = st.columns(3)


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
        "📚 Start Learning",
        use_container_width=True
    ):

        st.switch_page(
            "pages/learning.py"
        )


with col3:

    if st.button(
        "💼 Career Analysis",
        use_container_width=True
    ):

        st.switch_page(
            "pages/career.py"
        )
