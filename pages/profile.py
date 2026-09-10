import streamlit as st


st.set_page_config(
    page_title="EduTwin - Profile",
    page_icon="👤",
    layout="wide"
)


st.title("👤 My Learning Profile")

st.write(
    "Create your personal learning profile. "
    "EduTwin will use this information to build your Digital Twin."
)


st.divider()


# -----------------------------
# Personal Information
# -----------------------------

st.subheader("Personal Information")

name = st.text_input(
    "Full Name",
    placeholder="Enter your name"
)

education = st.text_input(
    "Education",
    placeholder="Example: BS Computer Science"
)


# -----------------------------
# Skills
# -----------------------------

st.subheader("💻 Skills")

skills_text = st.text_area(
    "Enter your skills",
    placeholder="Example: Python, C++, SQL, Machine Learning, Git",
    height=100
)


# -----------------------------
# Courses
# -----------------------------

st.subheader("📚 Courses")

courses_text = st.text_area(
    "Enter your courses",
    placeholder="Example: Data Structures, Artificial Intelligence, Database Systems",
    height=100
)


# -----------------------------
# Projects
# -----------------------------

st.subheader("🚀 Projects")

projects_text = st.text_area(
    "Enter your projects",
    placeholder="Example: AI Course Recommendation System, Carbon Calculator",
    height=100
)


# -----------------------------
# Interests
# -----------------------------

st.subheader("🎯 Interests")

interests_text = st.text_area(
    "What are you interested in?",
    placeholder="Example: Artificial Intelligence, Data Science, Computer Vision",
    height=100
)


# -----------------------------
# Career Goal
# -----------------------------

st.subheader("💼 Career Goal")

career_goal = st.selectbox(
    "What career are you interested in?",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Software Engineer",
        "Cybersecurity Engineer",
        "Cloud Engineer",
        "Other"
    ]
)


if career_goal == "Other":

    career_goal = st.text_input(
        "Enter your career goal",
        placeholder="Example: AI Researcher"
    )


st.divider()


# -----------------------------
# Save Profile
# -----------------------------

if st.button("💾 Save My Profile", type="primary"):

    if name.strip() == "":
        st.error("Please enter your name.")

    elif education.strip() == "":
        st.error("Please enter your education.")

    else:

        st.session_state["profile"] = {

            "name": name,

            "education": education,

            "skills": skills_text,

            "courses": courses_text,

            "projects": projects_text,

            "interests": interests_text,

            "career_goal": career_goal
        }

        st.success("✅ Your profile has been saved!")

        st.info(
            "Your profile will be used later to create your AI Digital Twin."
        )
