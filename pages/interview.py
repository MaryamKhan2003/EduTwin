import json

import streamlit as st

from ai.groq_client import ask_groq
from ai.prompts import build_interview_prompt


st.set_page_config(
    page_title="EduTwin - Interview",
    page_icon="🎤",
    layout="wide"
)


# --------------------------------------------------
# Check Digital Twin
# --------------------------------------------------

if "profile" not in st.session_state:

    st.title(" AI Interview Practice")

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


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title(" Interview AI")

    st.caption(
        "Practice for your future career"
    )

    st.divider()

    st.write(
        f" **{profile['name']}**"
    )

    st.write(
        f" {profile['career_goal']}"
    )

    st.divider()

    st.info(
        """
        EduTwin uses your Digital Twin
        to evaluate your interview answer.
        """
    )


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title(
    " AI Interview Practice"
)

st.subheader(
    "Practice like it's real."
)

st.write(
    """
    Answer an interview question and let
    EduTwin AI evaluate your response based
    on your target career and background.
    """
)

st.divider()


# --------------------------------------------------
# Target Career
# --------------------------------------------------

st.header(
    " Interview Target"
)

st.success(
    f"Target career: **{profile['career_goal']}**"
)


# --------------------------------------------------
# Question
# --------------------------------------------------

st.header(
    " Interview Question"
)

question = st.text_area(
    "Question",
    value=(
        f"Why do you want to become a "
        f"{profile['career_goal']}?"
    ),
    height=100
)


# --------------------------------------------------
# Answer
# --------------------------------------------------

st.header(
    " Your Answer"
)

answer = st.text_area(
    "Write your answer",
    placeholder=(
        "Answer as if you were sitting "
        "in a real interview..."
    ),
    height=180
)


# --------------------------------------------------
# Evaluation
# --------------------------------------------------

if st.button(
    " Evaluate My Answer",
    type="primary",
    use_container_width=True
):

    if question.strip() == "":

        st.warning(
            "Please enter an interview question."
        )

        st.stop()


    if answer.strip() == "":

        st.warning(
            "Please enter your answer first."
        )

        st.stop()


    try:

        if "GROQ_API_KEY" not in st.secrets:

            st.error(
                "GROQ_API_KEY is missing from "
                "Streamlit Secrets."
            )

            st.stop()


        # ------------------------------------------
        # Build AI prompt
        # ------------------------------------------

        prompt = build_interview_prompt(
            question,
            answer,
            profile
        )


        # ------------------------------------------
        # Call Groq
        # ------------------------------------------

        with st.spinner(
            " Groq AI is evaluating your answer..."
        ):

            result = ask_groq(
                prompt
            )


        # ------------------------------------------
        # Parse JSON
        # ------------------------------------------

        try:

            evaluation = json.loads(
                result
            )

        except json.JSONDecodeError:

            start = result.find("{")

            end = result.rfind("}")

            if start != -1 and end != -1:

                evaluation = json.loads(
                    result[start:end + 1]
                )

            else:

                raise ValueError(
                    "Groq returned an invalid evaluation format."
                )


        # ------------------------------------------
        # Save result
        # ------------------------------------------

        st.session_state[
            "interview_evaluation"
        ] = evaluation


        st.success(
            " Interview evaluation completed!"
        )


    except Exception as error:

        st.error(
            f" Interview AI error: {error}"
        )


# --------------------------------------------------
# Show Evaluation
# --------------------------------------------------

if "interview_evaluation" in st.session_state:

    evaluation = st.session_state[
        "interview_evaluation"
    ]


    st.divider()

    st.header(
        " AI Interview Evaluation"
    )


    # ----------------------------------------------
    # Scores
    # ----------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Overall",
            f"{evaluation.get('overall_score', 0)}/10"
        )


    with col2:

        st.metric(
            "Technical",
            f"{evaluation.get('technical_score', 0)}/10"
        )


    with col3:

        st.metric(
            "Communication",
            f"{evaluation.get('communication_score', 0)}/10"
        )


    with col4:

        st.metric(
            "Relevance",
            f"{evaluation.get('relevance_score', 0)}/10"
        )


    # ----------------------------------------------
    # Career alignment
    # ----------------------------------------------

    st.subheader(
        " Career Alignment"
    )

    career_score = evaluation.get(
        "career_alignment_score",
        0
    )

    st.progress(
        career_score / 10
    )

    st.write(
        f"**Career Alignment Score: "
        f"{career_score}/10**"
    )


    # ----------------------------------------------
    # Strengths
    # ----------------------------------------------

    st.divider()

    st.header(
        " Strengths"
    )

    strengths = evaluation.get(
        "strengths",
        []
    )


    if strengths:

        for strength in strengths:

            st.write(
                f" {strength}"
            )

    else:

        st.caption(
            "No specific strengths identified."
        )


    # ----------------------------------------------
    # Improvements
    # ----------------------------------------------

    st.header(
        " Areas for Improvement"
    )

    improvements = evaluation.get(
        "improvements",
        []
    )


    if improvements:

        for improvement in improvements:

            st.write(
                f" {improvement}"
            )

    else:

        st.caption(
            "No major improvements identified."
        )


    # ----------------------------------------------
    # Better Answer
    # ----------------------------------------------

    st.divider()

    st.header(
        " Suggested Better Answer"
    )

    better_answer = evaluation.get(
        "better_answer",
        ""
    )


    if better_answer:

        st.info(
            better_answer
        )

    else:

        st.caption(
            "No improved answer was generated."
        )


    # ----------------------------------------------
    # Final Feedback
    # ----------------------------------------------

    st.header(
        " Final AI Feedback"
    )

    final_feedback = evaluation.get(
        "final_feedback",
        ""
    )


    if final_feedback:

        st.write(
            final_feedback
        )

    else:

        st.caption(
            "No final feedback available."
        )
