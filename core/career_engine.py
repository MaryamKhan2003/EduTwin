import json

from core.skill_engine import calculate_skill_match


def load_careers():

    with open(
        "data/careers.json",
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


    normalized_user_skills = (
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
        normalized_user_skills,
        normalized_required_skills
    )


    return score
