def build_cv_analysis_prompt(cv_text):

    return f"""
You are EduTwin AI.

Analyze the following student's CV.

CV:
-------------------------
{cv_text}
-------------------------

Extract only information that is actually present.

Return the information using this structure:

Name:
Education:

Skills:
- skill 1
- skill 2

Courses:
- course 1
- course 2

Projects:
- project 1
- project 2

Interests:
- interest 1
- interest 2

Experience:
- experience 1

Certifications:
- certification 1

Possible Career Interests:
- career 1
- career 2

Do not invent information.
"""


def build_learning_prompt(topic, profile):

    return f"""
You are EduTwin AI, a personalized learning tutor.

Student name:
{profile["name"]}

Education:
{profile["education"]}

Skills:
{profile["skills"]}

Career goal:
{profile["career_goal"]}

Teach this student about:

{topic}

Create a beginner-friendly lesson.

Include:

1. Simple explanation
2. Important concepts
3. Practical example
4. Connection to the student's career
5. Short summary
6. Three questions to test understanding

Use simple language.
Do not assume advanced knowledge.
"""
