import json

from ai.groq_client import ask_groq_json
from ai.prompts import build_cv_analysis_prompt


def analyze_cv(cv_text):

    prompt = build_cv_analysis_prompt(
        cv_text
    )

    result = ask_groq_json(
        prompt
    )

    try:

        data = json.loads(
            result
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            "Groq returned invalid JSON for the CV analysis."
        ) from error


    # ----------------------------------------------
    # Make sure top-level sections exist
    # ----------------------------------------------

    if "profile" not in data:

        data["profile"] = {}


    if "analysis" not in data:

        data["analysis"] = {}


    profile = data["profile"]

    analysis = data["analysis"]


    # ----------------------------------------------
    # Profile defaults
    # ----------------------------------------------

    profile.setdefault(
        "name",
        ""
    )

    profile.setdefault(
        "education",
        ""
    )

    profile.setdefault(
        "skills",
        []
    )

    profile.setdefault(
        "courses",
        []
    )

    profile.setdefault(
        "projects",
        []
    )

    profile.setdefault(
        "interests",
        []
    )

    profile.setdefault(
        "experience",
        ""
    )

    profile.setdefault(
        "certifications",
        []
    )

    profile.setdefault(
        "career_goal",
        ""
    )


    # ----------------------------------------------
    # Analysis defaults
    # ----------------------------------------------

    analysis.setdefault(
        "profile_summary",
        ""
    )

    analysis.setdefault(
        "key_strengths",
        []
    )

    analysis.setdefault(
        "technical_strengths",
        []
    )

    analysis.setdefault(
        "skill_gaps",
        []
    )

    analysis.setdefault(
        "career_insight",
        ""
    )

    analysis.setdefault(
        "learning_recommendations",
        []
    )


    # ----------------------------------------------
    # Make sure list fields are lists
    # ----------------------------------------------

    profile_list_fields = [
        "skills",
        "courses",
        "projects",
        "interests",
        "certifications"
    ]


    for field in profile_list_fields:

        if not isinstance(
            profile[field],
            list
        ):

            if profile[field]:

                profile[field] = [
                    str(profile[field])
                ]

            else:

                profile[field] = []


    analysis_list_fields = [
        "key_strengths",
        "technical_strengths",
        "skill_gaps",
        "learning_recommendations"
    ]


    for field in analysis_list_fields:

        if not isinstance(
            analysis[field],
            list
        ):

            if analysis[field]:

                analysis[field] = [
                    str(analysis[field])
                ]

            else:

                analysis[field] = []


    return data
