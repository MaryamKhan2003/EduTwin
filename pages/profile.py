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

    st.title(" EduTwin AI")

    st.caption(
        "Digital Twin Builder"
    )

    st.divider()

    st.write(
        """
        ### Build your AI profile

         Upload CV

         AI Analysis

         Review information

         Create Digital Twin
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
    " Build Your Digital Twin"
)

st.subheader(
    "Let EduTwin understand you before it teaches you."
)

st.write(
    """
    Upload your CV and EduTwin will analyze your
    background, identify your strengths and skill gaps,
    and build the foundation of your Digital Twin.
    """
)

st.divider()


# ==================================================
# STEP 1 — UPLOAD CV
# ==================================================

st.header(
    " Step 1 — Upload Your CV"
)

st.write(
    """
    Upload your CV in PDF format. Groq AI will
    analyze the document and automatically extract
    your profile information.
    """
)


uploaded_cv = st.file_uploader(
    "Choose your CV",
    type=["pdf"],
    help="Upload your CV in PDF format."
)


if uploaded_cv is not None:

    st.success(
        f" {uploaded_cv.name} uploaded successfully."
    )


    if st.button(
        " Analyze My CV",
        type="primary",
        use_container_width=True
    ):

        try:

            # --------------------------------------
            # Check API key
            # --------------------------------------

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    " GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            if not st.secrets["GROQ_API_KEY"]:

                st.error(
                    " GROQ_API_KEY is empty."
                )

                st.stop()


            # --------------------------------------
            # Extract PDF text
            # --------------------------------------

            with st.spinner(
                " Reading your CV..."
            ):

                cv_text = extract_text_from_pdf(
                    uploaded_cv
                )


            if not cv_text.strip():

                st.error(
                    " No readable text was found "
                    "inside this PDF."
                )

                st.info(
                    """
                    This may be a scanned/image-only PDF.

                    Please use a CV PDF containing
                    selectable text.
                    """
                )

                st.stop()


            # --------------------------------------
            # Groq AI analysis
            # --------------------------------------

            with st.spinner(
                " Groq AI is analyzing your CV..."
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
                    " Groq returned an unexpected format."
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
                " CV analysis completed successfully!"
            )


        except Exception as error:

            st.error(
                f" CV analysis error: {error}"
            )


# ==================================================
# GET CV DATA
# ==================================================

cv_data = st.session_state.get(
    "cv_data",
    {}
)


profile_data = cv_data.get(
    "profile",
    {}
)


analysis_data = cv_data.get(
    "analysis",
    {}
)


# ==================================================
# HELPER
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
# AI ANALYSIS REPORT
# ==================================================

if cv_data:

    st.divider()

    st.header(
        " AI CV Analysis Report"
    )

    st.write(
        """
        EduTwin has analyzed your CV and created
        the following personalized profile insights.
        """
    )


    # ----------------------------------------------
    # Profile Summary
    # ----------------------------------------------

    st.subheader(
        " Profile Summary"
    )

    profile_summary = analysis_data.get(
        "profile_summary",
        ""
    )


    if profile_summary:

        st.info(
            profile_summary
        )

    else:

        st.caption(
            "No profile summary was generated."
        )


    # ----------------------------------------------
    # Strengths
    # ----------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            " Key Strengths"
        )

        strengths = analysis_data.get(
            "key_strengths",
            []
        )


        if strengths:

            for strength in strengths:

                st.write(
                    f" {strength}"
                )

        else:

            st.caption(
                "No strengths identified."
            )


    # ----------------------------------------------
    # Technical Strengths
    # ----------------------------------------------

    with col2:

        st.subheader(
            " Technical Strengths"
        )

        technical_strengths = analysis_data.get(
            "technical_strengths",
            []
        )


        if technical_strengths:

            for strength in technical_strengths:

                st.write(
                    f" {strength}"
                )

        else:

            st.caption(
                "No technical strengths identified."
            )


    # ----------------------------------------------
    # Skill Gaps
    # ----------------------------------------------

    st.subheader(
        " Skill Gaps"
    )

    skill_gaps = analysis_data.get(
        "skill_gaps",
        []
    )


    if skill_gaps:

        for gap in skill_gaps:

            st.write(
                f" {gap}"
            )

    else:

        st.success(
            "No major skill gaps were identified from the CV."
        )


    # ----------------------------------------------
    # Career Insight
    # ----------------------------------------------

    st.subheader(
        " Career Insight"
    )

    career_insight = analysis_data.get(
        "career_insight",
        ""
    )


    if career_insight:

        st.success(
            career_insight
        )

    else:

        st.caption(
            "No career insight was generated."
        )


    # ----------------------------------------------
    # Learning Recommendations
    # ----------------------------------------------

    st.subheader(
        " Recommended Learning Areas"
    )

    recommendations = analysis_data.get(
        "learning_recommendations",
        []
    )


    if recommendations:

        for recommendation in recommendations:

            st.write(
                f" {recommendation}"
            )

    else:

        st.caption(
            "No learning recommendations were generated."
        )


# ==================================================
# STEP 2 — REVIEW PROFILE
# ==================================================

st.divider()

st.header(
    " Step 2 — Review Your Extracted Information"
)

st.caption(
    """
    Groq AI automatically extracted this information
    from your CV. You can edit anything before
    creating your Digital Twin.
    """
)


# ==================================================
# BASIC INFORMATION
# ==================================================

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Full Name",
        value=profile_data.get(
            "name",
            ""
        ),
        placeholder="Example: Maryam Khan"
    )


with col2:

    education = st.text_input(
        "Education",
        value=profile_data.get(
            "education",
            ""
        ),
        placeholder="Example: BS Computer Science"
    )


# ==================================================
# SKILLS
# ==================================================

st.subheader(
    " Skills"
)

skills = st.text_area(
    "Your Skills",
    value=list_to_text(
        profile_data.get(
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
    " Courses"
)

courses = st.text_area(
    "Courses You Have Studied",
    value=list_to_text(
        profile_data.get(
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
    " Projects"
)

projects = st.text_area(
    "Your Projects",
    value=list_to_text(
        profile_data.get(
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
    " Interests"
)

interests = st.text_area(
    "Your Interests",
    value=list_to_text(
        profile_data.get(
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
        " Experience",
        value=profile_data.get(
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
        " Certifications",
        value=list_to_text(
            profile_data.get(
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
# CAREER
# ==================================================

st.subheader(
    " Target Career"
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


detected_career = profile_data.get(
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
    " Step 3 — Create Your Digital Twin"
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
        # Save Digital Twin
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
            " Your Digital Twin has been created!"
        )

        st.balloons()


        # ------------------------------------------
        # Profile summary
        # ------------------------------------------

        st.divider()

        st.header(
            " Your Digital Twin"
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
                " Skills",
                len(skill_list)
            )


        with col2:

            st.metric(
                " Courses",
                len(course_list)
            )


        with col3:

            st.metric(
                " Projects",
                len(project_list)
            )


        st.success(
            f" Target Career: {career_goal}"
        )


        st.write("")


        if st.button(
            " Open My Dashboard",
            use_container_width=True
        ):

            st.switch_page(
                "pages/dashboard.py"
            )
