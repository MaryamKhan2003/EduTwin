import streamlit as st

from ai.groq_client import ask_groq


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

        prompt = f"""
You are an AI interview coach.

Student name:
{profile["name"]}

Education:
{profile["education"]}

Skills:
{profile["skills"]}

Career goal:
{profile["career_goal"]}

Interview question:
{question}

Student answer:
{answer}

Evaluate the answer.

Give:

1. Overall evaluation
2. What was good
3. What can be improved
4. Technical/content suggestions
5. Communication suggestions
6. A better sample answer

Be supportive and educational.
"""


        try:

            with st.spinner(
                "AI is evaluating your answer..."
            ):

                evaluation = ask_groq(
                    prompt
                )


            st.subheader(
                "🤖 AI Interview Feedback"
            )


            st.markdown(
                evaluation
            )


        except Exception as error:

            st.error(
                f"Interview AI error: {error}"
            )
