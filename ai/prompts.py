def build_cv_analysis_prompt(cv_text):

    return f"""
You are EduTwin AI.

You are analyzing a student's CV for an AI-powered
Personal Digital Twin.

Your task has TWO purposes:

1. Extract accurate information from the CV.
2. Analyze the student's current skills, strengths,
   career direction and learning needs.

CV:
-------------------------
{cv_text}
-------------------------

Return ONLY one valid JSON object.

Use exactly this structure:

{{
    "profile": {{
        "name": "",
        "education": "",
        "skills": [],
        "courses": [],
        "projects": [],
        "interests": [],
        "experience": "",
        "certifications": [],
        "career_goal": ""
    }},

    "analysis": {{
        "profile_summary": "",
        "key_strengths": [],
        "technical_strengths": [],
        "skill_gaps": [],
        "career_insight": "",
        "learning_recommendations": []
    }}
}}

IMPORTANT RULES:

1. Only use information supported by the CV.

2. Do not invent education, skills, projects,
   experience or certifications.

3. If information is missing, use an empty string
   or an empty list.

4. Skills must be a list of short skill names.

5. Courses must be a list.

6. Projects must be a list.

7. Interests must be a list.

8. Certifications must be a list.

9. Experience must be a single string.

10. Education must be a single string.

11. career_goal should only be filled if the CV
    clearly indicates a target career or the
    career can reasonably be inferred from the
    student's education, skills and projects.

12. profile_summary should be a short professional
    summary of the student's background.

13. key_strengths should contain 3 to 5 strengths
    supported by the CV.

14. technical_strengths should contain technical
    areas where the student appears strongest.

15. skill_gaps should identify important skills
    that appear missing or underdeveloped based
    ONLY on the student's current profile.

16. career_insight should explain which career
    directions appear suitable based on the CV.

17. learning_recommendations should contain
    3 to 5 practical areas the student should
    learn or improve next.

18. Do not make unsupported claims.

19. Do not use markdown.

20. Do not put the JSON inside ```json fences.

21. Return ONLY the JSON object.
"""


def build_learning_prompt(topic, profile):

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

Keep the response below 600 words.
"""


def build_interview_prompt(question, answer, profile):

    return f"""
You are EduTwin AI Interview Coach.

Evaluate a student's interview answer.

STUDENT:

Name:
{profile['name']}

Education:
{profile['education']}

Skills:
{profile['skills']}

Target Career:
{profile['career_goal']}

Interests:
{profile['interests']}


INTERVIEW QUESTION:

{question}


STUDENT ANSWER:

{answer}


Evaluate the answer based on:

1. Technical knowledge
2. Relevance
3. Communication
4. Clarity
5. Confidence
6. Career alignment


Return ONLY a valid JSON object using exactly:

{{
    "overall_score": 0,
    "technical_score": 0,
    "communication_score": 0,
    "relevance_score": 0,
    "career_alignment_score": 0,
    "strengths": [],
    "improvements": [],
    "better_answer": "",
    "final_feedback": ""
}}

Scoring:

0 = very weak
1-3 = needs major improvement
4-5 = below average
6-7 = acceptable
8-9 = strong
10 = excellent

Rules:

- Be honest but constructive.
- Do not invent experience.
- Do not give a high score simply because the answer is long.
- strengths must be a list.
- improvements must be a list.
- Scores must be between 0 and 10.
- The better answer must be realistic.
- Base the better answer only on the student's information.
- Return only JSON.
"""
