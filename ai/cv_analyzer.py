
from ai.groq_client import ask_groq

from ai.prompts import build_cv_analysis_prompt


def analyze_cv(cv_text):

    prompt = build_cv_analysis_prompt(
        cv_text
    )


    result = ask_groq(
        prompt
    )


    return result
