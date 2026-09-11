import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from ai.cv_analyzer import analyze_cv


st.set_page_config(
    page_title="EduTwin - Profile",
    page_icon="👤",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("👤 Build Your Digital Twin")

st.subheader(
    "Let EduTwin understand you before it teaches you."
)

st.write(
    """
    Upload your CV and EduTwin AI will analyze your
    education, skills, projects, experience and interests
    to create your personalized learning profile.
    """
)

st.divider()


# --------------------------------------------------
# CV UPLOAD
# --------------------------------------------------

st.header("📄 Step 1 — Upload Your CV")

st.write(
    "Upload your CV in PDF format. EduTwin will extract "
    "the relevant information automatically."
)

uploaded_cv = st.file_uploader(
    "Choose your CV",
    type=["pdf"],
    help="Upload a PDF CV for AI analysis."
)


# --------------------------------------------------
# ANALYZE CV BUTTON
# --------------------------------------------------

if uploaded_cv is not None:

    st.success(
        f"✅ CV uploaded: {uploaded_cv.name}"
    )

    st.info(
        "Your CV will be analyzed by EduTwin AI. "
        "You can review and edit the extracted information "
        "before creating your Digital Twin."
    )

    if st.button(
        "🤖 Analyze My CV",
        type="primary",
        use_container_width=True
    ):

        try:

            # ------------------------------------------
            # CHECK GROQ API KEY
            # ------------------------------------------

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            # ------------------------------------------
            # EXTRACT TEXT FROM PDF
            # ------------------------------------------

            with st.spinner(
                "📄 Reading your CV..."
            ):

                cv_text = extract_text_from_pdf(
                    uploaded_cv
                )


            # ------------------------------------------
            # CHECK CV TEXT
            # ------------------------------------------

            if not cv_text.strip():

                st.error(
                    "❌ No readable text was found in the CV."
                )

                st.info(
                    """
                    Please make sure your PDF contains
                    selectable text. Scanned/image-only PDFs
                    may not be readable by the current parser.
                    """
                )

                st.stop()


            # ------------------------------------------
            # SEND CV TO GROQ
            # ------------------------------------------

            with st.spinner(
                "🧠 EduTwin AI is analyzing your CV..."
            ):

                analysis = analyze_cv(
                    cv_text
                )


            # ------------------------------------------
            # SAVE AI RESULT
            # ------------------------------------------

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


# --------------------------------------------------
# SHOW AI ANALYSIS
# --------------------------------------------------

if "cv_analysis" in st.session_state:

    st.divider()

    st.header(
        "🧠 Step 2 — AI CV Analysis"
    )

    st.write(
        """
        EduTwin extracted the following information
        from your CV.
        """
    )

    with st.expander(
        "🔍 View AI Analysis",
        expanded=True
    ):

        st.markdown(
            st.session_state["cv_analysis"]
        )

    st.info(
        """
        💡 Review the AI analysis above, then enter
        or correct your information in the profile
        fields below.
        """
    )


# --------------------------------------------------
# MANUAL PROFILE SECTION
# --------------------------------------------------

st.divider()

st.header(
    "✏️ Step 3 — Confirm Your Digital Twin"
)

st.write(
    """
    You can manually enter or correct any information
    before creating your Digital Twin.
    """
)


# --------------------------------------------------
# PERSONAL INFORMATION
# --------------------------------------------------

st.subheader("🎓 Personal Information")

name = st.text_input(
    "Full Name",
    placeholder="Example: Maryam Khan"
)

education = st.text_input(
    "Education",
    placeholder="Example: BS Computer Science"
)


# --------------------------------------------------
# SKILLS
# --------------------------------------------------

st.subheader("💻 Skills")

skills = st.text_area(
    "Your Skills",
    placeholder=(
        "Example: Python, C++, SQL, Machine Learning, "
        "Data Structures, Git"
    ),
    height=120
)


# --------------------------------------------------
# COURSES
# --------------------------------------------------

st.subheader("📚 Courses")

courses = st.text_area(
    "Courses You Have Studied",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Data Structures, Database Systems"
    ),
    height=120
)


# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

st.subheader("🚀 Projects")

projects = st.text_area(
    "Your Projects",
    placeholder=(
        "Example: AI Course Recommendation System, "
        "Carbon Calculator"
    ),
    height=120
)


# --------------------------------------------------
# INTERESTS
# --------------------------------------------------

st.subheader("💡 Interests")

interests = st.text_area(
    "Your Interests",
    placeholder=(
        "Example: Artificial Intelligence, "
        "Machine Learning, Data Science"
    ),
    height=120
)


# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

st.subheader("💼 Experience")

experience = st.text_area(
    "Work / Internship Experience",
    placeholder=(
        "Example: Software Engineering Intern, "
        "Research Assistant"
    ),
    height=120
)


# --------------------------------------------------
# CERTIFICATIONS
# --------------------------------------------------

st.subheader("🏆 Certifications")

certifications = st.text_area(
    "Certifications",
    placeholder=(
        "Example: Python Certification, "
        "Google Data Analytics"
    ),
    height=100
)


# --------------------------------------------------
# CAREER GOAL
# --------------------------------------------------

st.subheader("🎯 Career Goal")

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


# --------------------------------------------------
# CREATE DIGITAL TWIN
# --------------------------------------------------

st.divider()

st.header(
    "🧠 Create Your Digital Twin"
)

st.write(
    """
    Once you confirm your information, EduTwin will
    create your personalized Digital Twin.
    """
)


if st.button(
    "🧠 Create My Digital Twin",
    type="primary",
    use_container_width=True
):

    # ----------------------------------------------
    # VALIDATION
    # ----------------------------------------------

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

        # ------------------------------------------
        # CREATE PROFILE
        # ------------------------------------------

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


        # ------------------------------------------
        # SUCCESS MESSAGE
        # ------------------------------------------

        st.success(
            "🎉 Your Digital Twin has been created!"
        )

        st.balloons()


        # ------------------------------------------
        # PROFILE SUMMARY
        # ------------------------------------------

        st.divider()

        st.header(
            "📋 Your Digital Twin Summary"
        )

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "👤 Personal Profile"
            )

            st.write(
                f"**Name:** {name}"
            )

            st.write(
                f"**Education:** {education}"
            )

            st.write(
                f"**Career Goal:** {career_goal}"
            )

            st.write(
                f"**Skills:** {skills}"
            )


        with col2:

            st.subheader(
                "🚀 Learning Profile"
            )

            st.write(
                f"**Courses:** {courses}"
            )

            st.write(
                f"**Projects:** {projects}"
            )

            st.write(
                f"**Interests:** {interests}"
            )

            st.write(
                f"**Experience:** {experience}"
            )

            st.write(
                f"**Certifications:** {certifications}"
            )


        st.divider()

        st.info(
            """
            🎯 Your Digital Twin is now ready.

            You can use it with:

            📷 Vision Tutor  
            📚 Adaptive Learning  
            💼 Career Intelligence  
            🎤 AI Interview Practice
            """
        )
