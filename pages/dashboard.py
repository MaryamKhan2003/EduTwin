import streamlit as st


st.set_page_config(
    page_title="EduTwin - Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Digital Twin Dashboard")


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


st.subheader(
    f"Welcome, {profile['name']} 👋"
)


st.write(
    "This dashboard shows your current Digital Twin."
)


st.divider()


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


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Career Goal",
        profile["career_goal"]
    )


with col2:

    st.metric(
        "Skills",
        len(skills)
    )


with col3:

    st.metric(
        "Courses",
        len(courses)
    )


st.divider()


st.header("👤 Digital Twin")


st.write(
    f"**Education:** {profile['education']}"
)


st.write(
    f"**Skills:** {profile['skills']}"
)


st.write(
    f"**Courses:** {profile['courses']}"
)


st.write(
    f"**Projects:** {profile['projects']}"
)


st.write(
    f"**Interests:** {profile['interests']}"
)


st.write(
    f"**Career Goal:** {profile['career_goal']}"
)


st.divider()


st.header("🧠 Twin Status")


st.success(
    "Your Digital Twin is active."
)


st.info(
    """
    As you use Vision Tutor, Learning, Career Analysis,
    quizzes, and Interview Practice, the Digital Twin
    can later be updated with your learning progress.
    """
)
