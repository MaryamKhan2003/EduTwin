import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin - Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==================================================
# PROFILE CHECK
# ==================================================

if "profile" not in st.session_state:

    st.title(
        "📊 Your Dashboard"
    )

    st.warning(
        "Your Digital Twin has not been created yet."
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


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title(
        "🧠 EduTwin AI"
    )

    st.caption(
        "Personal Learning Dashboard"
    )

    st.divider()

    st.write(
        f"👋 **{profile['name']}**"
    )

    st.write(
        f"🎯 {profile['career_goal']}"
    )

    st.divider()

    st.write(
        "Use the pages below to continue your journey."
    )


# ==================================================
# HEADER
# ==================================================

st.title(
    f"Good to see you, {profile['name']} 👋"
)

st.subheader(
    "Your personalized learning command center."
)

st.write(
    """
    Track your profile, explore new concepts,
    analyze your career and prepare for interviews.
    """
)

st.divider()


# ==================================================
# DATA
# ==================================================

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


# ==================================================
# TOP METRICS
# ==================================================

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


# ==================================================
# DIGITAL TWIN PROFILE
# ==================================================

st.divider()

st.header(
    "👤 Your Digital Twin"
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
        "💻 Core Skills"
    )

    for skill in skills:

        st.write(
            f"✅ {skill}"
        )


with col2:

    st.subheader(
        "🎯 Career Direction"
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


# ==================================================
# COURSES + PROJECTS
# ==================================================

st.divider()

col1, col2 = st.columns(2)


with col1:

    st.header(
        "📚 Learning Background"
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


# ==================================================
# QUICK ACTIONS
# ==================================================

st.divider()

st.header(
    "⚡ Continue Your Journey"
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


# ==================================================
# DIGITAL TWIN MESSAGE
# ==================================================

st.divider()

st.header(
    "🧠 Your AI Learning Loop"
)

st.info(
    """
    **Know yourself → Learn → Practice → Identify gaps
    → Improve → Move closer to your career goal**
    """
)
