
import streamlit as st


st.set_page_config(
    page_title="EduTwin - Learning",
    page_icon="📚",
    layout="wide"
)


st.title("📚 Adaptive Learning")


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


st.write(
    f"Learning recommendations for {profile['name']}"
)


st.divider()


topic = st.text_input(
    "What do you want to learn?",
    placeholder="Example: Neural Networks"
)


if st.button(
    "📖 Start Learning",
    type="primary"
):

    if topic.strip() == "":

        st.warning(
            "Please enter a topic."
        )

    else:

        st.subheader(
            f"Learning Topic: {topic}"
        )


        st.write(
            f"""
            EduTwin will create a personalized lesson
            for **{profile['career_goal']}** learners.
            """
        )


        st.info(
            "AI-generated lessons will be connected here next."
        )
