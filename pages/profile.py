import streamlit as st

from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Profile",
    page_icon="👤",
    layout="wide"
)


load_css()


# =========================================
# HERO
# =========================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-small">
            STEP 01 • BUILD YOUR DIGITAL TWIN
        </div>

        <div class="hero-title">
            Tell EduTwin about you. 👤
        </div>

        <div class="hero-text">
            Your education, skills, projects, interests and
            career goals help EduTwin create a personalized
            learning experience.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# PERSONAL INFORMATION
# =========================================

st.markdown(
    '<div class="section-label">YOUR INFORMATION</div>',
    unsafe_allow_html=True
)

st.header(
    "🎓 Personal Information"
)


name = st.text_input(
    "Full Name",
    placeholder="Enter your full name"
)


education = st.text_input(
    "Education",
    placeholder="Example: BS Computer Science"
)


# =========================================
# SKILLS
# =========================================

st.header(
    "💻 Your Skills"
)


skills = st.text_area(
    "Skills",
    placeholder=(
        "Example: Python, C++, SQL, Machine Learning, "
        "Data Structures, Git"
    ),
    height=120
)


# =========================================
# COURSES
# =========================================

st.header(
    "📚 Courses"
)


courses = st.text_area(
    "Courses You Have Studied",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Data Structures, Database Systems"
    ),
    height=120
)


# =========================================
# PROJECTS
# =========================================

st.header(
    "🚀 Projects"
)


projects = st.text_area(
    "Your Projects",
    placeholder=(
        "Example: AI Course Recommendation System, "
        "Carbon Calculator"
    ),
    height=120
)


# =========================================
# INTERESTS
# =========================================

st.header(
    "💡 Interests"
)


interests = st.text_area(
    "Your Interests",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Machine Learning, Data Science"
    ),
    height=120
)


# =========================================
# CAREER
# =========================================

st.header(
    "🎯 Career Goal"
)


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


# =========================================
# SAVE PROFILE
# =========================================

if st.button(
    "💾 Save My Digital Twin",
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
            "Please enter your target career."
        )

    else:

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
            "✅ Your Digital Twin has been created!"
        )


        st.balloons()


        st.markdown(
            """
            <div class="insight-card">

                <div class="insight-title">
                    🧠 Your Digital Twin is ready
                </div>

                <div class="insight-text">
                    EduTwin can now personalize your
                    learning, vision explanations and
                    career analysis using your profile.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


        col1, col2 = st.columns(2)


        with col1:

            st.write(
                f"**Name:** {name}"
            )

            st.write(
                f"**Education:** {education}"
            )

            st.write(
                f"**Career:** {career_goal}"
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
            "Your profile is now available to EduTwin's "
            "learning and career features."
        )
