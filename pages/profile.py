import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from ai.cv_analyzer import analyze_cv


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin - Digital Twin",
    page_icon="👤",
    layout="wide"
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🧠 EduTwin AI")

    st.caption(
        "Digital Twin Builder"
    )

    st.divider()

    st.write(
        """
        ### Build your AI profile

        📄 Upload CV

        🤖 AI Analysis

        ✏️ Confirm information

        🧠 Create Digital Twin
        """
    )

    st.divider()

    st.info(
        "Your profile powers personalized learning."
    )


# ==================================================
# HEADER
# ==================================================

st.title(
    "👤 Build Your Digital Twin"
)

st.subheader(
    "Let EduTwin understand you before it teaches you."
)

st.write(
    """
    Your Digital Twin represents your **education,
    skills, courses, projects, experience, interests
    and career goals**.
    """
)

st.divider()


# ==================================================
# STEP 1 — CV
# ==================================================

st.header(
    "📄 Step 1 — Upload Your CV"
)

st.write(
    """
    Upload your CV in PDF format. Groq AI will analyze
    it and extract information about your background.
    """
)

uploaded_cv = st.file_uploader(
    "Choose your CV",
    type=["pdf"],
    help="Upload a PDF CV for AI analysis."
)


if uploaded_cv is not None:

    st.success(
        f"✅ {uploaded_cv.name} uploaded successfully."
    )

    if st.button(
        "🤖 Analyze My CV",
        type="primary",
        use_container_width=True
    ):

        try:

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            with st.spinner(
                "📄 Reading your CV..."
            ):

                cv_text = extract_text_from_pdf(
                    uploaded_cv
                )


            if not cv_text.strip():

                st.error(
                    "❌ No readable text was found in the CV."
                )

                st.stop()


            with st.spinner(
                "🧠 Groq AI is analyzing your CV..."
            ):

                analysis = analyze_cv(
                    cv_text
                )


            st.session_state[
                "cv_analysis"
            ] = analysis

            st.session_state[
                "cv_text"
            ] = cv_text

            st.success(
                "✅ CV analysis completed!"
            )


        except Exception as error:

            st.error(
                f"❌ CV analysis error: {error}"
            )


# ==================================================
# AI ANALYSIS
# ==================================================

if "cv_analysis" in st.session_state:

    st.divider()

    st.header(
        "🧠 AI Analysis"
    )

    with st.expander(
        "🔍 View extracted CV information",
        expanded=True
    ):

        st.markdown(
            st.session_state["cv_analysis"]
        )

    st.info(
        """
        Review the AI analysis and confirm your
        information in the profile fields below.
        """
    )


# ==================================================
# STEP 2 — PROFILE
# ==================================================

st.divider()

st.header(
    "✏️ Step 2 — Confirm Your Information"
)

st.caption(
    "You can edit any information before creating your Digital Twin."
)


# ==================================================
# PERSONAL INFORMATION
# ==================================================

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Full Name",
        placeholder="Example: Maryam Khan"
    )


with col2:

    education = st.text_input(
        "Education",
        placeholder="Example: BS Computer Science"
    )


# ==================================================
# SKILLS
# ==================================================

st.subheader(
    "💻 Skills"
)

skills = st.text_area(
    "Your Skills",
    placeholder=(
        "Python, C++, SQL, Machine Learning, "
        "Data Structures, Git"
    ),
    height=110
)


# ==================================================
# COURSES
# ==================================================

st.subheader(
    "📚 Courses"
)

courses = st.text_area(
    "Courses You Have Studied",
    placeholder=(
        "Artificial Intelligence, Data Structures, "
        "Database Systems"
    ),
    height=100
)


# ==================================================
# PROJECTS
# ==================================================

st.subheader(
    "🚀 Projects"
)

projects = st.text_area(
    "Your Projects",
    placeholder=(
        "AI Course Recommendation System, "
        "Carbon Calculator"
    ),
    height=100
)


# ==================================================
# INTERESTS
# ==================================================

st.subheader(
    "💡 Interests"
)

interests = st.text_area(
    "Your Interests",
    placeholder=(
        "Artificial Intelligence, Machine Learning, "
        "Data Science"
    ),
    height=100
)


# ==================================================
# EXPERIENCE + CERTIFICATIONS
# ==================================================

col1, col2 = st.columns(2)


with col1:

    experience = st.text_area(
        "💼 Experience",
        placeholder=(
            "Internships, jobs, research experience..."
        ),
        height=120
    )


with col2:

    certifications = st.text_area(
        "🏆 Certifications",
        placeholder=(
            "Python Certification, Google Data Analytics..."
        ),
        height=120
    )


# ==================================================
# CAREER
# ==================================================

st.subheader(
    "🎯 Target Career"
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
    "What career are you working toward?",
    career_options
)


if career_goal == "Other":

    career_goal = st.text_input(
        "Enter your target career",
        placeholder="Example: AI Researcher"
    )


# ==================================================
# CREATE DIGITAL TWIN
# ==================================================

st.divider()

st.header(
    "🧠 Step 3 — Create Your Digital Twin"
)

if st.button(
    "Create My Digital Twin →",
    type="primary",
    use_container_width=True
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

            "experience": experience.strip(),

            "certifications": certifications.strip(),

            "career_goal": career_goal.strip()
        }


        st.success(
            "🎉 Your Digital Twin has been created!"
        )

        st.balloons()


        # ------------------------------------------
        # SUMMARY
        # ------------------------------------------

        st.divider()

        st.header(
            "✨ Your Digital Twin"
        )

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "💻 Skills",
                len(
                    [
                        x for x in skills.split(",")
                        if x.strip()
                    ]
                )
            )


        with col2:

            st.metric(
                "📚 Courses",
                len(
                    [
                        x for x in courses.split(",")
                        if x.strip()
                    ]
                )
            )


        with col3:

            st.metric(
                "🚀 Projects",
                len(
                    [
                        x for x in projects.split(",")
                        if x.strip()
                    ]
                )
            )


        st.success(
            f"🎯 Target Career: {career_goal}"
        )


        st.write("")

        if st.button(
            "📊 Open My Dashboard",
            use_container_width=True
        ):

            st.switch_page(
                "pages/dashboard.py"
            )
