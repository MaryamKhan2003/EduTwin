def calculate_skill_match(user_skills, required_skills):

    total = 0
    achieved = 0

    for skill, required_level in required_skills.items():

        total += required_level

        user_level = user_skills.get(skill, 0)

        achieved += min(user_level, required_level)

    if total == 0:
        return 0

    return round((achieved / total) * 100, 2)
