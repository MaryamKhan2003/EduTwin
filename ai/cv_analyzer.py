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


    # Make sure all expected fields exist

    data.setdefault(
        "name",
        ""
    )

    data.setdefault(
        "education",
        ""
    )

    data.setdefault(
        "skills",
        []
    )

    data.setdefault(
        "courses",
        []
    )

    data.setdefault(
        "projects",
        []
    )

    data.setdefault(
        "interests",
        []
    )

    data.setdefault(
        "experience",
        ""
    )

    data.setdefault(
        "certifications",
        []
    )

    data.setdefault(
        "career_goal",
        ""
    )


    # Make sure list fields are actually lists

    list_fields = [
        "skills",
        "courses",
        "projects",
        "interests",
        "certifications"
    ]


    for field in list_fields:

        if not isinstance(
            data[field],
            list
        ):

            data[field] = [
                str(data[field])
            ]


    return data
