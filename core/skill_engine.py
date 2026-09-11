def clean_skills(skills_text):

    if not skills_text:
        return []

    skills = skills_text.split(",")

    cleaned_skills = []

    for skill in skills:

        skill = skill.strip()

        if skill:
            cleaned_skills.append(skill)

    return cleaned_skills


def calculate_skill_match(
    user_skills,
    required_skills
):

    if not required_skills:
        return 0

    total_score = 0
    achieved_score = 0

    for skill, required_level in required_skills.items():

        total_score += required_level

        user_level = user_skills.get(
            skill,
            0
        )

        achieved_score += min(
            user_level,
            required_level
        )

    if total_score == 0:
        return 0

    percentage = (
        achieved_score /
        total_score
    ) * 100

    return round(
        percentage,
        2
    )


def find_skill_gaps(
    user_skills,
    required_skills
):

    gaps = []

    for skill, required_level in required_skills.items():

        user_level = user_skills.get(
            skill,
            0
        )

        if user_level < required_level:

            gaps.append(
                {
                    "skill": skill,
                    "current": user_level,
                    "required": required_level,
                    "gap": (
                        required_level -
                        user_level
                    )
                }
            )

    return gaps
