import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="EduTwin - Profile",
    page_icon="👤",
    layout="wide"
)


# -----------------------------
# Page Title
# -----------------------------

st.title("👤 My Learning Profile")

st.write(
    """
    Create your personal learning profile.
    EduTwin will use this information to build your Digital Twin.
    """
)


st.divider()


# -----------------------------
# Personal Information
# -----------------------------

st.header("Personal Information")


name = st.text_input(
    "Full Name",
    placeholder="Enter your full name"
)


education = st.text_input(
    "Education",
    placeholder="Example: BS Computer Science"
)


# -----------------------------
# Skills
# -----------------------------

st.header("💻 Skills")


skills = st.text_area(
    "Your Skills",
    placeholder=(
        "Example: Python, C++, SQL, Machine Learning, "
        "Data Structures, Git"
    ),
    height=120
)


# -----------------------------
# Courses
# -----------------------------

st.header("📚 Courses")


courses = st.text_area(
    "Courses You Have Studied",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Data Structures, Database Systems"
    ),
    height=120
)


# -----------------------------
# Projects
# -----------------------------

st.header("🚀 Projects")


projects = st.text_area(
    "Your Projects",
    placeholder=(
        "Example: AI Course Recommendation System, "
        "Carbon Calculator"
    ),
    height=120
)


# -----------------------------
# Interests
# -----------------------------

st.header("🎯 Interests")


interests = st.text_area(
    "Your Interests",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Machine Learning, Data Science"
    ),
    height=120
)


# -----------------------------
# Career Goal
# -----------------------------

st.header("💼 Career Goal")


career_options = [
    "AI Engineer",
    "Machine Learning Engineer",
    "Data Scientist",
    "Data Analyst",
    "Software Engineer",
    "Cybersecurity Engineer",
    "Cloud Engineer",
    "Other"
]


career_goal = st.selectbox(
    "Select your target career",
    career_options
)


if career_goal == "Other":

    career_goal = st.text_input(
        "Enter your target career",
        placeholder="Example: AI Researcher"
    )


st.divider()


# -----------------------------
# Save Profile
# -----------------------------

if st.button(
    "💾 Save My Profile",
    type="primary"
):

    if name.strip() == "":

        st.error("Please enter your name.")

    elif education.strip() == "":

        st.error("Please enter your education.")

    elif skills.strip() == "":

        st.error("Please enter at least one skill.")

    else:

        # Store profile in Streamlit session

        st.session_state["profile"] = {

            "name": name.strip(),

            "education": education.strip(),

            "skills": skills.strip(),

            "courses": courses.strip(),

            "projects": projects.strip(),

            "interests": interests.strip(),

            "career_goal": career_goal.strip()
        }


        st.success(
            "✅ Your profile has been saved successfully!"
        )


        st.subheader("Your Profile Summary")


        col1, col2 = st.columns(2)


        with col1:

            st.write(
                f"**Name:** {name}"
            )

            st.write(
                f"**Education:** {education}"
            )

            st.write(
                f"**Career Goal:** {career_goal}"
            )


        with col2:

            st.write(
                f"**Skills:** {skills}"
            )

            st.write(
                f"**Courses:** {courses}"
            )

            st.write(
                f"**Interests:** {interests}"
            )


        st.info(
            "Your information will be used later by Groq AI "
            "to create your Digital Twin."
        )
