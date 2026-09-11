
def build_cv_analysis_prompt(cv_text):

    prompt = f"""
You are EduTwin AI.

Your job is to analyze a student's CV and create a structured
student learning profile.

Read the CV below carefully.

CV:
-------------------------
{cv_text}
-------------------------

Extract the following information:

1. Name
2. Education
3. Skills
4. Courses
5. Projects
6. Interests
7. Work experience
8. Certifications
9. Possible career interests

Return the result using exactly this structure:

Name:
Education:

Skills:
- skill 1
- skill 2
- skill 3

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

Only include information supported by the CV.
Do not invent information.
"""

    return prompt

def build_learning_prompt(
    topic,
    profile
):

    return f"""
You are EduTwin AI, a personalized learning tutor.

Student:
{profile['name']}

Education:
{profile['education']}

Skills:
{profile['skills']}

Career goal:
{profile['career_goal']}

Teach the student about:

{topic}

Create a beginner-friendly lesson.

The lesson should contain:

1. Simple explanation
2. Important concepts
3. Practical example
4. Connection to the student's career
5. Short summary
6. Three questions to test understanding

Do not assume the student already knows advanced concepts.
"""
