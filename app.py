import streamlit as st


st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 EduTwin AI")

st.subheader(
    "Your Personal AI Learning and Career Twin"
)


st.write(
    """
    EduTwin AI creates a personalized digital representation
    of your skills, knowledge, interests, and career goals.
    """
)


st.divider()


st.header("Welcome to EduTwin")


st.write(
    """
    EduTwin helps you understand what you know, identify
    what you need to learn, and prepare for your desired career.
    """
)


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("👤 Digital Twin")

    st.write(
        """
        Build a personalized profile containing your
        skills, courses, projects, interests, and career goal.
        """
    )


with col2:

    st.subheader("📷 Vision Tutor")

    st.write(
        """
        Upload an educational image and let AI identify
        and explain what you are looking at.
        """
    )


with col3:

    st.subheader("💼 Career AI")

    st.write(
        """
        Analyze your skills, identify skill gaps,
        and understand your career readiness.
        """
    )


st.divider()


if "profile" in st.session_state:

    profile = st.session_state["profile"]

    st.success(
        f"Welcome back, {profile['name']}! "
        f"Your target career is {profile['career_goal']}."
    )

else:

    st.info(
        "👈 Open **Profile** from the sidebar to create "
        "your Digital Twin."
    )
