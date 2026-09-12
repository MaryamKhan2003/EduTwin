import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from ai.cv_analyzer import analyze_cv


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

        ✏️ Review information

        🧠 Create Digital Twin
        """
    )

    st.divider()

    st.info(
        "Your profile powers personalized learning."
    )


# ==================================================
# PAGE HEADER
# ==================================================

st.title(
    "👤 Build Your Digital Twin"
)

st.subheader(
    "Let EduTwin understand you before it teaches you."
)

st.write(
    """
    Upload your CV and EduTwin will use AI to
    understand your education, skills, projects,
    experience and career direction.
    """
)

st.divider()


# ==================================================
# STEP 1 — CV UPLOAD
# ==================================================

st.header(
    "📄 Step 1 — Upload Your CV"
)

st.write(
    """
    Upload a PDF CV. EduTwin will extract the text
    and use Groq AI to automatically identify your
    profile information.
    """
)


uploaded_cv = st.file_uploader(
    "Choose your CV",
    type=["pdf"],
    help="Upload your CV in PDF format."
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

            # --------------------------------------
            # Check API key
            # --------------------------------------

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "❌ GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            if not st.secrets["GROQ_API_KEY"]:

                st.error(
                    "❌ GROQ_API_KEY is empty."
                )

                st.stop()


            # --------------------------------------
            # Extract PDF text
            # --------------------------------------

            with st.spinner(
                "📄 Reading your CV..."
            ):

                cv_text = extract_text_from_pdf(
                    uploaded_cv
                )


            if not cv_text.strip():

                st.error(
                    "❌ No readable text was found "
                    "inside this PDF."
                )

                st.info(
                    """
                    Please make sure your CV contains
                    selectable text. A scanned image-only
                    PDF may not contain extractable text.
                    """
                )

                st.stop()


            # --------------------------------------
            # Analyze with Groq
            # --------------------------------------

            with st.spinner(
                "🧠 Groq AI is analyzing your CV..."
            ):

                cv_data = analyze_cv(
                    cv_text
                )


            # --------------------------------------
            # Validate result
            # --------------------------------------

            if not isinstance(
                cv_data,
                dict
            ):

                st.error(
                    "❌ Groq returned an unexpected data format."
                )

                st.stop()


            # --------------------------------------
            # Save result
            # --------------------------------------

            st.session_state[
                "cv_data"
            ] = cv_data

            st.session_state[
                "cv_text"
            ] = cv_text


            st.success(
                "✅ CV analyzed successfully!"
            )

            st.info(
                """
                🎯 Your profile fields have been
                automatically filled using your CV.

                Review the information below.
                You can edit anything before creating
                your Digital Twin.
                """
            )


        except Exception as error:

            st.error(
                f"❌ CV analysis error: {error}"
            )


# ==================================================
# LOAD CV DATA
# ==================================================

cv_data = st.session_state.get(
    "cv_data",
    {}
)


# ==================================================
# HELPER FUNCTION
# ==================================================

def list_to_text(items):

    if not items:
        return ""

    if isinstance(
        items,
        str
    ):
        return items

    return ", ".join(
        str(item)
        for item in items
        if str(item).strip()
    )


# ==================================================
# STEP 2 — REVIEW INFORMATION
# ==================================================

st.divider()

st.header(
    "✏️ Step 2 — Review Your Information"
)

st.caption(
    "Groq AI automatically fills these fields from "
    "your CV. You can edit them before creating "
    "your Digital Twin."
)


# ==================================================
# BASIC INFORMATION
# ==================================================

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Full Name",
        value=cv_data.get(
            "name",
            ""
        ),
        placeholder="Example: Maryam Khan"
    )


with col2:

    education = st.text_input(
        "Education",
        value=cv_data.get(
            "education",
            ""
        ),
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
    value=list_to_text(
        cv_data.get(
            "skills",
            []
        )
    ),
    placeholder=(
        "Python, C++, SQL, Machine Learning..."
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
    value=list_to_text(
        cv_data.get(
            "courses",
            []
        )
    ),
    placeholder=(
        "Artificial Intelligence, "
        "Data Structures..."
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
    value=list_to_text(
        cv_data.get(
            "projects",
            []
        )
    ),
    placeholder=(
        "AI Course Recommendation System, "
        "Carbon Calculator..."
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
    value=list_to_text(
        cv_data.get(
            "interests",
            []
        )
    ),
    placeholder=(
        "Artificial Intelligence, "
        "Machine Learning..."
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
        value=cv_data.get(
            "experience",
            ""
        ),
        placeholder=(
            "Internships, jobs, research experience..."
        ),
        height=120
    )


with col2:

    certifications = st.text_area(
        "🏆 Certifications",
        value=list_to_text(
            cv_data.get(
                "certifications",
                []
            )
        ),
        placeholder=(
            "Python Certification, "
            "Google Data Analytics..."
        ),
        height=120
    )


# ==================================================
# TARGET CAREER
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


detected_career = cv_data.get(
    "career_goal",
    ""
)


if detected_career in career_options:

    default_index = career_options.index(
        detected_career
    )

else:

    default_index = 0


career_goal = st.selectbox(
    "What career are you working toward?",
    career_options,
    index=default_index
)


if career_goal == "Other":

    custom_career = st.text_input(
        "Enter your target career",
        value=(
            detected_career
            if detected_career not in career_options
            else ""
        ),
        placeholder="Example: AI Researcher"
    )

    career_goal = custom_career


# ==================================================
# STEP 3 — CREATE DIGITAL TWIN
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

        # ------------------------------------------
        # Create profile
        # ------------------------------------------

        st.session_state[
            "profile"
        ] = {

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
        # Summary
        # ------------------------------------------

        st.divider()

        st.header(
            "✨ Your Digital Twin"
        )


        skill_list = [
            x.strip()
            for x in skills.split(",")
            if x.strip()
        ]


        course_list = [
            x.strip()
            for x in courses.split(",")
            if x.strip()
        ]


        project_list = [
            x.strip()
            for x in projects.split(",")
            if x.strip()
        ]


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "💻 Skills",
                len(skill_list)
            )


        with col2:

            st.metric(
                "📚 Courses",
                len(course_list)
            )


        with col3:

            st.metric(
                "🚀 Projects",
                len(project_list)
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
