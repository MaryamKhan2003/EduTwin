
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
