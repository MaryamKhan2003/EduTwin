import streamlit as st

from ai.cv_analyzer import analyze_cv
from utils.pdf_parser import (
    extract_text_from_pdf
)


st.set_page_config(
    page_title="EduTwin - Profile",
    page_icon="👤",
    layout="wide"
)


st.title("👤 My Learning Profile")


st.write(
    """
    Create your personal Digital Twin.
    You can manually enter your information or
    upload a CV for AI analysis.
    """
)


st.divider()


st.header("📄 Upload CV")


cv_file = st.file_uploader(
    "Upload your CV as a PDF",
    type=["pdf"]
)


if cv_file is not None:

    if st.button(
        "🤖 Analyze My CV",
        type="secondary"
    ):

        try:

            cv_text = extract_text_from_pdf(
                cv_file
            )

            if not cv_text:

                st.warning(
                    "No readable text was found in the PDF."
                )

            else:

                with st.spinner(
                    "Groq AI is analyzing your CV..."
                ):

                    result = analyze_cv(
                        cv_text
                    )

                st.subheader(
                    "🤖 AI CV Analysis"
                )

                st.markdown(result)

        except Exception as error:

            st.error(
                f"CV analysis error: {error}"
            )


st.divider()


st.header("Personal Information")


name = st.text_input(
    "Full Name",
    placeholder="Enter your full name"
)


education = st.text_input(
    "Education",
    placeholder="Example: BS Computer Science"
)


st.header("💻 Skills")


skills = st.text_area(
    "Your Skills",
    placeholder=(
        "Example: Python, C++, SQL, "
        "Machine Learning, Git"
    ),
    height=120
)


st.header("📚 Courses")


courses = st.text_area(
    "Courses You Have Studied",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Data Structures, Database Systems"
    ),
    height=120
)


st.header("🚀 Projects")


projects = st.text_area(
    "Your Projects",
    placeholder=(
        "Example: AI Course Recommendation System, "
        "Carbon Calculator"
    ),
    height=120
)


st.header("🎯 Interests")


interests = st.text_area(
    "Your Interests",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Machine Learning, Data Science"
    ),
    height=120
)


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


if st.button(
    "💾 Save My Profile",
    type="primary"
):

    if name.strip() == "":

        st.error(
            "Please enter your name."
        )

    elif education.strip() == "":

        st.error(
            "Please enter your education."
        )

    elif skills.strip() == "":

        st.error(
            "Please enter at least one skill."
        )

    elif career_goal.strip() == "":

        st.error(
            "Please enter your career goal."
        )

    else:

        profile = {
            "name": name.strip(),
            "education": education.strip(),
            "skills": skills.strip(),
            "courses": courses.strip(),
            "projects": projects.strip(),
            "interests": interests.strip(),
            "career_goal": career_goal.strip()
        }

        st.session_state["profile"] = profile

        st.success(
            "✅ Your Digital Twin profile has been saved!"
        )

        st.subheader(
            "👤 Your Profile Summary"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Name:** {profile['name']}"
            )

            st.write(
                f"**Education:** {profile['education']}"
            )

            st.write(
                f"**Career Goal:** {profile['career_goal']}"
            )

            st.write(
                f"**Skills:** {profile['skills']}"
            )

        with col2:

            st.write(
                f"**Courses:** {profile['courses']}"
            )

            st.write(
                f"**Projects:** {profile['projects']}"
            )

            st.write(
                f"**Interests:** {profile['interests']}"
            )
