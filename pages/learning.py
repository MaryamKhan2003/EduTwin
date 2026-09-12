import streamlit as st

from ai.groq_client import ask_groq
from ai.prompts import build_learning_prompt


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin - Learning",
    page_icon="📚",
    layout="wide"
)


# ==================================================
# PROFILE CHECK
# ==================================================

if "profile" not in st.session_state:

    st.title(
        " Adaptive Learning"
    )

    st.warning(
        "Create your Digital Twin first."
    )

    if st.button(
        " Create My Digital Twin",
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )

    st.stop()


profile = st.session_state["profile"]


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title(
        " Adaptive Learning"
    )

    st.caption(
        "Your personalized AI tutor"
    )

    st.divider()

    st.write(
        f" **{profile['name']}**"
    )

    st.write(
        f" {profile['career_goal']}"
    )


# ==================================================
# HEADER
# ==================================================

st.title(
    " Adaptive Learning"
)

st.subheader(
    "Learn something that matters to your future."
)

st.write(
    """
    EduTwin creates lessons based on your
    existing skills, knowledge and career goal.
    """
)

st.divider()


# ==================================================
# DIGITAL TWIN
# ==================================================

with st.expander(
    " What EduTwin knows about you",
    expanded=False
):

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Education:** {profile['education']}"
        )

        st.write(
            f"**Skills:** {profile['skills']}"
        )

    with col2:

        st.write(
            f"**Career:** {profile['career_goal']}"
        )

        st.write(
            f"**Interests:** {profile['interests']}"
        )


# ==================================================
# TOPIC
# ==================================================

st.header(
    " What do you want to learn?"
)

topic = st.text_input(
    "Learning Topic",
    placeholder=(
        "Example: Neural Networks, SQL Joins, "
        "Cloud Computing..."
    )
)


# ==================================================
# GENERATE
# ==================================================

if st.button(
    " Start Personalized Learning",
    type="primary",
    use_container_width=True
):

    if topic.strip() == "":

        st.warning(
            "Please enter a learning topic first."
        )

    else:

        try:

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            prompt = build_learning_prompt(
                topic,
                profile
            )


            with st.spinner(
                " EduTwin is preparing your lesson..."
            ):

                lesson = ask_groq(
                    prompt
                )


            st.success(
                " Your personalized lesson is ready!"
            )

            st.divider()

            st.header(
                f" {topic}"
            )

            st.markdown(
                lesson
            )


            st.divider()

            st.info(
                """
                 **Keep learning!**

                After understanding this topic,
                the next version of EduTwin can
                test your knowledge and update
                your learning profile.
                """
            )


        except Exception as error:

            st.error(
                f" Learning AI error: {error}"
            )
