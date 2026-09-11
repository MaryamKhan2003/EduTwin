import json
from pathlib import Path

from core.skill_engine import (
    calculate_skill_match
)


BASE_DIR = Path(__file__).resolve().parent.parent

CAREERS_FILE = (
    BASE_DIR /
    "data" /
    "careers.json"
)


def load_careers():

    with open(
        CAREERS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def normalize_skill_name(skill):

    return skill.strip().lower()


def create_user_skill_dictionary(
    skills
):

    user_skills = {}

    for skill in skills:

        user_skills[
            normalize_skill_name(skill)
        ] = 100

    return user_skills


def calculate_career_readiness(
    skills,
    career_name
):

    careers = load_careers()

    if career_name not in careers:
        return 0

    required_skills = careers[
        career_name
    ]

    user_skills = (
        create_user_skill_dictionary(
            skills
        )
    )

    normalized_required_skills = {}

    for skill, level in required_skills.items():

        normalized_required_skills[
            normalize_skill_name(skill)
        ] = level

    score = calculate_skill_match(
        user_skills,
        normalized_required_skills
    )

    return score


def get_skill_gaps(
    skills,
    career_name
):

    careers = load_careers()

    if career_name not in careers:
        return []

    required_skills = careers[
        career_name
    ]

    user_skills = (
        create_user_skill_dictionary(
            skills
        )
    )

    gaps = []

    for skill, required_level in required_skills.items():

        normalized_skill = (
            normalize_skill_name(skill)
        )

        current_level = user_skills.get(
            normalized_skill,
            0
        )

        if current_level < required_level:

            gaps.append(
                {
                    "skill": skill,
                    "current": current_level,
                    "required": required_level,
                    "gap": (
                        required_level -
                        current_level
                    )
                }
            )

    return gaps
