
def create_learning_recommendations(
    skill_gaps
):

    recommendations = []


    for gap in skill_gaps:

        skill = gap["skill"]

        recommendations.append(
            f"Improve your {skill} skills."
        )


    return recommendations
