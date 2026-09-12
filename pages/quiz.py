# ==================================================
# EDUTWIN AI QUIZ & ASSESSMENT
# ==================================================

import streamlit as st

from core.quiz_engine import (
    generate_quiz,
    calculate_score,
    analyze_quiz_result
)


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="EduTwin - Quiz",
    page_icon="📝",
    layout="wide"
)


# ==================================================
# CHECK DIGITAL TWIN
# ==================================================

if "profile" not in st.session_state:

    st.title(
        "📝 AI Quiz & Assessment"
    )

    st.warning(
        "You need to create your Digital Twin first."
    )


    if st.button(
        "👤 Create My Digital Twin",
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
        "🧠 EduTwin AI"
    )

    st.caption(
        "Adaptive Learning Assessment"
    )

    st.divider()


    st.write(
        f"👤 **{profile['name']}**"
    )


    st.write(
        f"🎯 **Career:** "
        f"{profile['career_goal']}"
    )


    st.divider()


    st.write(
        """
        ### How it works

        📚 Choose a topic

        🤖 AI generates 5 questions

        📝 Answer the questions

        📊 Get your score

        ⚠️ Discover weak areas

        🚀 Get personalized recommendations
        """
    )


    st.divider()


    st.info(
        """
        Your quiz performance helps
        EduTwin understand what you
        need to learn next.
        """
    )


# ==================================================
# PAGE HEADER
# ==================================================

st.title(
    "📝 AI Quiz & Assessment"
)

st.subheader(
    "Test what you actually learned."
)

st.write(
    """
    EduTwin generates five personalized questions
    based on your selected topic and Digital Twin.
    After the quiz, AI identifies your weak areas
    and recommends your next learning step.
    """
)

st.divider()


# ==================================================
# STEP 1 — SELECT TOPIC
# ==================================================

st.header(
    "📚 Step 1 — Choose a Topic"
)


skills_text = profile.get(
    "skills",
    ""
)


courses_text = profile.get(
    "courses",
    ""
)


# ==================================================
# CONVERT SKILLS INTO LIST
# ==================================================

skills_list = []


if isinstance(
    skills_text,
    str
):

    skills_list = [
        item.strip()
        for item in skills_text.split(",")
        if item.strip()
    ]

elif isinstance(
    skills_text,
    list
):

    skills_list = [
        str(item).strip()
        for item in skills_text
        if str(item).strip()
    ]


# ==================================================
# CONVERT COURSES INTO LIST
# ==================================================

courses_list = []


if isinstance(
    courses_text,
    str
):

    courses_list = [
        item.strip()
        for item in courses_text.split(",")
        if item.strip()
    ]

elif isinstance(
    courses_text,
    list
):

    courses_list = [
        str(item).strip()
        for item in courses_text
        if str(item).strip()
    ]


# ==================================================
# CREATE TOPIC LIST
# ==================================================

topic_options = []


for item in skills_list:

    if item not in topic_options:

        topic_options.append(
            item
        )


for item in courses_list:

    if item not in topic_options:

        topic_options.append(
            item
        )


# ==================================================
# DEFAULT TOPICS
# ==================================================

if not topic_options:

    topic_options = [
        "Python",
        "Object Oriented Programming",
        "Data Structures",
        "Artificial Intelligence"
    ]


topic_options.append(
    "Custom Topic"
)


selected_topic = st.selectbox(
    "What would you like to practice?",
    topic_options
)


# ==================================================
# CUSTOM TOPIC
# ==================================================

if selected_topic == "Custom Topic":

    topic = st.text_input(
        "Enter your topic",
        placeholder="Example: Python Functions"
    )

else:

    topic = selected_topic


# ==================================================
# STEP 2 — GENERATE QUIZ
# ==================================================

st.header(
    "🤖 Step 2 — Generate Your Quiz"
)


if st.button(
    "🤖 Generate My 5-Question Quiz",
    type="primary",
    use_container_width=True
):

    if not topic.strip():

        st.warning(
            "⚠️ Please select or enter a topic."
        )

        st.stop()


    try:

        # ------------------------------------------
        # Check Groq API key
        # ------------------------------------------

        if "GROQ_API_KEY" not in st.secrets:

            st.error(
                "❌ GROQ_API_KEY is missing from "
                "Streamlit Secrets."
            )

            st.stop()


        if not st.secrets[
            "GROQ_API_KEY"
        ]:

            st.error(
                "❌ GROQ_API_KEY is empty."
            )

            st.stop()


        # ------------------------------------------
        # Generate quiz
        # ------------------------------------------

        with st.spinner(
            "🧠 Groq AI is creating your personalized quiz..."
        ):

            quiz = generate_quiz(
                topic,
                profile
            )


        # ------------------------------------------
        # Save quiz
        # ------------------------------------------

        st.session_state[
            "quiz"
        ] = quiz


        st.session_state[
            "quiz_topic"
        ] = topic


        # ------------------------------------------
        # Clear previous results
        # ------------------------------------------

        st.session_state.pop(
            "quiz_score",
            None
        )


        st.session_state.pop(
            "quiz_analysis",
            None
        )


        st.session_state.pop(
            "quiz_wrong_questions",
            None
        )


        st.success(
            "✅ Your personalized quiz is ready!"
        )


    except Exception as error:

        st.error(
            f"❌ Quiz generation error: {error}"
        )


# ==================================================
# DISPLAY GENERATED QUIZ
# ==================================================

if "quiz" in st.session_state:

    quiz = st.session_state[
        "quiz"
    ]


    quiz_topic = st.session_state[
        "quiz_topic"
    ]


    st.divider()


    st.header(
        f"🧠 Quiz: {quiz_topic}"
    )


    st.caption(
        "Answer all five questions before submitting."
    )


    # ----------------------------------------------
    # Student answers
    # ----------------------------------------------

    user_answers = {}


    # ==================================================
    # QUESTIONS
    # ==================================================

    for index, question in enumerate(
        quiz["questions"]
    ):

        st.subheader(
            f"Question {index + 1}"
        )


        st.write(
            question["question"]
        )


        options = question[
            "options"
        ]


        selected_answer = st.radio(
            "Choose one answer:",
            options,
            key=f"quiz_question_{index}",
            index=None
        )


        if selected_answer is not None:

            user_answers[index] = (
                options.index(
                    selected_answer
                )
            )


        st.divider()


    # ==================================================
    # SUBMIT QUIZ
    # ==================================================

    if st.button(
        "📊 Submit Quiz",
        type="primary",
        use_container_width=True
    ):

        # ------------------------------------------
        # Check all questions answered
        # ------------------------------------------

        if len(user_answers) != 5:

            st.warning(
                "⚠️ Please answer all 5 questions "
                "before submitting."
            )

            st.stop()


        # ------------------------------------------
        # Calculate score
        # ------------------------------------------

        score, wrong_questions = calculate_score(
            quiz["questions"],
            user_answers
        )


        st.session_state[
            "quiz_score"
        ] = score


        st.session_state[
            "quiz_wrong_questions"
        ] = wrong_questions


        # ------------------------------------------
        # Analyze performance using Groq
        # ------------------------------------------

        try:

            with st.spinner(
                "🤖 EduTwin AI is analyzing your performance..."
            ):

                analysis = analyze_quiz_result(
                    quiz_topic,
                    score,
                    5,
                    wrong_questions,
                    profile
                )


            st.session_state[
                "quiz_analysis"
            ] = analysis


            st.success(
                "✅ Quiz evaluated successfully!"
            )


        except Exception as error:

            st.error(
                f"❌ AI analysis error: {error}"
            )


# ==================================================
# QUIZ RESULT
# ==================================================

if "quiz_score" in st.session_state:

    score = st.session_state[
        "quiz_score"
    ]


    # ----------------------------------------------
    # Calculate percentage
    # ----------------------------------------------

    percentage = int(
        (score / 5) * 100
    )


    # ----------------------------------------------
    # Determine performance
    # ----------------------------------------------

    if percentage >= 80:

        local_performance = "Strong"

    elif percentage >= 60:

        local_performance = "Good"

    elif percentage >= 40:

        local_performance = "Needs Practice"

    else:

        local_performance = "Weak"


    st.divider()


    st.header(
        "📊 Your Quiz Result"
    )


    # ==================================================
    # SCORE CARDS
    # ==================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🏆 Score",
            f"{score}/5"
        )


    with col2:

        st.metric(
            "📈 Percentage",
            f"{percentage}%"
        )


    with col3:

        st.metric(
            "🧠 Performance",
            local_performance
        )


    # ==================================================
    # PROGRESS BAR
    # ==================================================

    st.progress(
        percentage / 100
    )


    # ==================================================
    # RESULT MESSAGE
    # ==================================================

    if percentage >= 80:

        st.success(
            "🎉 Excellent! You have a strong understanding of this topic."
        )

    elif percentage >= 60:

        st.info(
            "👍 Good work! You understand the main concepts, but there is still room for improvement."
        )

    elif percentage >= 40:

        st.warning(
            "📚 You understand some concepts, but this topic needs more practice."
        )

    else:

        st.error(
            "⚠️ This topic needs significant improvement. EduTwin recommends reviewing the fundamentals."
        )


# ==================================================
# INCORRECT QUESTIONS
# ==================================================

if "quiz_wrong_questions" in st.session_state:

    wrong_questions = st.session_state[
        "quiz_wrong_questions"
    ]


    if wrong_questions:

        st.divider()


        st.header(
            "⚠️ Questions You Missed"
        )


        for index, item in enumerate(
            wrong_questions
        ):

            with st.expander(
                f"Question {index + 1}"
            ):

                st.write(
                    f"**Question:** "
                    f"{item['question']}"
                )


                st.write(
                    f"❌ **Your answer:** "
                    f"{item['student_answer']}"
                )


                st.write(
                    f"✅ **Correct answer:** "
                    f"{item['correct_answer']}"
                )


# ==================================================
# AI LEARNING ANALYSIS
# ==================================================

if "quiz_analysis" in st.session_state:

    analysis = st.session_state[
        "quiz_analysis"
    ]


    st.divider()


    st.header(
        "🤖 EduTwin AI Learning Analysis"
    )


    # ==================================================
    # PERFORMANCE LEVEL
    # ==================================================

    performance_level = analysis.get(
        "performance_level",
        ""
    )


    st.subheader(
        "🧠 AI Performance Assessment"
    )


    if performance_level == "Strong":

        st.success(
            f"🌟 {performance_level}"
        )

    elif performance_level == "Good":

        st.info(
            f"👍 {performance_level}"
        )

    elif performance_level == "Needs Practice":

        st.warning(
            f"📚 {performance_level}"
        )

    elif performance_level == "Weak":

        st.error(
            f"⚠️ {performance_level}"
        )

    else:

        st.info(
            "Performance assessment unavailable."
        )


    # ==================================================
    # WEAK TOPICS
    # ==================================================

    st.subheader(
        "⚠️ Weak Areas"
    )


    weak_topics = analysis.get(
        "weak_topics",
        []
    )


    if weak_topics:

        for weak_topic in weak_topics:

            st.write(
                f"🔸 {weak_topic}"
            )

    else:

        st.success(
            "No major weak areas were identified."
        )


    # ==================================================
    # RECOMMENDATION
    # ==================================================

    st.subheader(
        "🚀 Personalized Recommendation"
    )


    recommendation = analysis.get(
        "recommendation",
        ""
    )


    if recommendation:

        st.info(
            recommendation
        )

    else:

        st.caption(
            "No recommendation was generated."
        )


    # ==================================================
    # NEXT LEARNING STEP
    # ==================================================

    st.subheader(
        "📚 Recommended Next Learning Step"
    )


    next_step = analysis.get(
        "next_learning_step",
        ""
    )


    if next_step:

        st.success(
            next_step
        )

    else:

        st.caption(
            "No next learning step was generated."
        )


# ==================================================
# RETAKE QUIZ
# ==================================================

if "quiz" in st.session_state:

    st.divider()


    if st.button(
        "🔄 Generate Another Quiz",
        use_container_width=True
    ):

        # ------------------------------------------
        # Remove old quiz
        # ------------------------------------------

        st.session_state.pop(
            "quiz",
            None
        )


        st.session_state.pop(
            "quiz_topic",
            None
        )


        st.session_state.pop(
            "quiz_score",
            None
        )


        st.session_state.pop(
            "quiz_analysis",
            None
        )


        st.session_state.pop(
            "quiz_wrong_questions",
            None
        )


        # ------------------------------------------
        # Remove old radio answers
        # ------------------------------------------

        for index in range(5):

            key = (
                f"quiz_question_{index}"
            )


            if key in st.session_state:

                del st.session_state[key]


        st.rerun()
