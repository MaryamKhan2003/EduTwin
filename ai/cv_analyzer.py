import json

from ai.groq_client import ask_groq
from ai.prompts import build_cv_analysis_prompt


def analyze_cv(cv_text):

    prompt = build_cv_analysis_prompt(cv_text)

    result = ask_groq(prompt)

    try:
        data = json.loads(result)

        return data

    except json.JSONDecodeError:

        # Try to recover JSON if Groq added extra text
        start = result.find("{")
        end = result.rfind("}")

        if start != -1 and end != -1:

            json_text = result[start:end + 1]

            return json.loads(json_text)

        raise ValueError(
            "Groq returned an invalid CV analysis format."
        )
