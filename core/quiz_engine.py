# ==================================================
# EDUTWIN QUIZ ENGINE
# ==================================================

import json

from ai.groq_client import ask_groq_json

from ai.prompts import (
    build_quiz_prompt,
    build_quiz_analysis_prompt
)


# ==================================================
# GENERATE QUIZ
# ==================================================

def generate_quiz(
    topic,
    profile
):

    prompt = build_quiz_prompt(
        topic,
        profile
    )


    result = ask_groq_json(
        prompt
    )


    # ----------------------------------------------
    # Convert JSON text into Python dictionary
    # ----------------------------------------------

    try:

        quiz = json.loads(
            result
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            "Groq returned invalid JSON for the quiz."
        ) from error


    # ----------------------------------------------
    # Check questions section
    # ----------------------------------------------

    if "questions" not in quiz:

        raise ValueError(
            "Groq did not return quiz questions."
        )


    questions = quiz["questions"]


    if not isinstance(
        questions,
        list
    ):

        raise ValueError(
            "Quiz questions are not in list format."
        )


    # ----------------------------------------------
    # Exactly 5 questions
    # ----------------------------------------------

    if len(questions) != 5:

        raise ValueError(
            "Groq did not generate exactly 5 questions."
        )


    # ----------------------------------------------
    # Validate each question
    # ----------------------------------------------

    for question_number, question in enumerate(
        questions,
        start=1
    ):

        if not isinstance(
            question,
            dict
        ):

            raise ValueError(
                f"Question {question_number} "
                "has an invalid format."
            )


        if "question" not in question:

            raise ValueError(
                f"Question {question_number} "
                "is missing its question text."
            )


        if "options" not in question:

            raise ValueError(
                f"Question {question_number} "
                "is missing its options."
            )


        if "answer" not in question:

            raise ValueError(
                f"Question {question_number} "
                "is missing its correct answer."
            )


        options = question["options"]


        if not isinstance(
            options,
            list
        ):

            raise ValueError(
                f"Question {question_number} "
                "options are not in list format."
            )


        if len(options) != 4:

            raise ValueError(
                f"Question {question_number} "
                "does not have exactly 4 options."
            )


        answer = question["answer"]


        if answer not in [
            0,
            1,
            2,
            3
        ]:

            raise ValueError(
                f"Question {question_number} "
                "has an invalid correct answer."
            )


    return quiz


# ==================================================
# CALCULATE QUIZ SCORE
# ==================================================

def calculate_score(
    questions,
    user_answers
):

    score = 0

    wrong_questions = []


    # ----------------------------------------------
    # Check every question
    # ----------------------------------------------

    for index, question in enumerate(
        questions
    ):

        correct_answer = question["answer"]


        user_answer = user_answers.get(
            index
        )


        # ------------------------------------------
        # Correct answer
        # ------------------------------------------

        if user_answer == correct_answer:

            score += 1


        # ------------------------------------------
        # Wrong / unanswered answer
        # ------------------------------------------

        else:

            if user_answer is not None:

                student_answer = (
                    question["options"][
                        user_answer
                    ]
                )

            else:

                student_answer = (
                    "Not answered"
                )


            correct_answer_text = (
                question["options"][
                    correct_answer
                ]
            )


            wrong_questions.append(
                {
                    "question":
                        question["question"],

                    "student_answer":
                        student_answer,

                    "correct_answer":
                        correct_answer_text
                }
            )


    return (
        score,
        wrong_questions
    )


# ==================================================
# ANALYZE QUIZ PERFORMANCE WITH GROQ
# ==================================================

def analyze_quiz_result(
    topic,
    score,
    total,
    wrong_questions,
    profile
):

    # ----------------------------------------------
    # Prepare incorrect questions
    # ----------------------------------------------

    if wrong_questions:

        wrong_text = ""


        for item in wrong_questions:

            wrong_text += (
                f"Question: "
                f"{item['question']}\n"
            )

            wrong_text += (
                f"Student Answer: "
                f"{item['student_answer']}\n"
            )

            wrong_text += (
                f"Correct Answer: "
                f"{item['correct_answer']}\n\n"
            )


    else:

        wrong_text = (
            "The student answered every "
            "question correctly."
        )


    # ----------------------------------------------
    # Build AI prompt
    # ----------------------------------------------

    prompt = build_quiz_analysis_prompt(
        topic,
        score,
        total,
        wrong_text,
        profile
    )


    # ----------------------------------------------
    # Ask Groq
    # ----------------------------------------------

    result = ask_groq_json(
        prompt
    )


    # ----------------------------------------------
    # Parse JSON
    # ----------------------------------------------

    try:

        analysis = json.loads(
            result
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            "Groq returned invalid JSON "
            "for quiz analysis."
        ) from error


    # ----------------------------------------------
    # Ensure required fields exist
    # ----------------------------------------------

    analysis.setdefault(
        "performance_level",
        ""
    )


    analysis.setdefault(
        "weak_topics",
        []
    )


    analysis.setdefault(
        "recommendation",
        ""
    )


    analysis.setdefault(
        "next_learning_step",
        ""
    )


    # ----------------------------------------------
    # Make sure weak topics is a list
    # ----------------------------------------------

    if not isinstance(
        analysis["weak_topics"],
        list
    ):

        if analysis["weak_topics"]:

            analysis["weak_topics"] = [
                str(
                    analysis["weak_topics"]
                )
            ]

        else:

            analysis["weak_topics"] = []


    return analysis
