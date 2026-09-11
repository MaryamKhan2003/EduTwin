import streamlit as st


st.set_page_config(
    page_title="EduTwin - Interview",
    page_icon="🎤",
    layout="wide"
)


st.title("🎤 AI Interview Practice")


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


st.write(
    f"""
    Practice interview questions for your target career:
    **{profile['career_goal']}**
    """
)


st.divider()


question = st.text_area(
    "Interview Question",
    value=(
        f"Why do you want to become a "
        f"{profile['career_goal']}?"
    ),
    height=100
)


answer = st.text_area(
    "Your Answer",
    placeholder="Type your answer here...",
    height=200
)


if st.button(
    "🎯 Evaluate My Answer",
    type="primary"
):

    if answer.strip() == "":

        st.warning(
            "Please enter your answer first."
        )

    else:

        st.success(
            "Answer received!"
        )


        st.info(
            "AI interview evaluation will be connected here next."
        )
