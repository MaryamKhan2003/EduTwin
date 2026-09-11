import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="EduTwin AI",
    page_icon="🧠",
    layout="wide"
)


# -----------------------------
# Main Page
# -----------------------------

st.title("🧠 EduTwin AI")

st.subheader("Your Personal AI Learning Twin")

st.write(
    """
    EduTwin AI creates a personalized digital representation
    of your skills, knowledge, interests, and career goals.
    """
)


st.divider()


# -----------------------------
# Welcome Section
# -----------------------------

st.header("Welcome to EduTwin")

st.write(
    """
    EduTwin helps you understand what you know, identify what
    you need to learn, and prepare for your desired career.
    """
)


# -----------------------------
# Features
# -----------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("👤 Digital Twin")

    st.write(
        "Build a personalized profile containing your "
        "skills, courses, projects, interests, and career goal."
    )


with col2:

    st.subheader("📷 Vision Tutor")

    st.write(
        "Upload an educational image and let AI explain "
        "what you are looking at."
    )


with col3:

    st.subheader("💼 Career AI")

    st.write(
        "Analyze your skills and identify gaps for your "
        "target career."
    )


st.divider()


st.info(
    "👈 Use the sidebar to open your profile and start building "
    "your Digital Twin."
)
