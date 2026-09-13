#  EduTwin AI

## An AI-Powered Personal Digital Twin for Adaptive Multimodal Learning and Career Development

EduTwin AI is an AI-powered educational platform that creates a **Personal Digital Twin of a student** based on their skills, education, courses, projects, interests, experience, and career goals.

Instead of providing the same learning experience to every student, EduTwin AI first tries to understand **who the student is, what they already know, what they want to achieve, and where they have knowledge gaps**.

The system then uses Generative AI to provide personalized learning, visual explanations, quizzes, weak-topic detection, career guidance, and interview practice.

> **EduTwin AI doesn't just teach the student. It first understands the student, then teaches, tests, evaluates, and recommends what to learn next.**

---
Project OverviewTraditional learning systems often follow a one-size-fits-all approach.Every student may receive:The same learning materialThe same explanationsThe same difficulty levelThe same quiz questionsThe same learning pathHowever, students have different:Knowledge levelsTechnical skillsInterestsAcademic backgroundsCareer goalsLearning difficultiesEduTwin AI addresses this problem by creating a student-specific Digital Twin. The Digital Twin becomes the foundation for personalized AI interactions.Basic ConceptPlaintextStudent Information
       ↓
CV / Profile
       ↓
AI Profile Analysis
       ↓
Personal Digital Twin
       ↓
Personalized Learning
       ↓
AI Quiz
       ↓
Performance Analysis
       ↓
Weak Topic Detection
       ↓
Learning Recommendation
       ↓
Updated Learning Direction
Problem StatementStudents often struggle to identify:What skills they already haveWhich skills are missing for their desired careerWhich topics they are weak inWhat they should learn nextHow to understand complex technical diagrams and conceptsWhether they are actually improvingHow prepared they are for interviewsMost educational platforms provide general content without considering the student's complete profile.The main problem is: How can AI provide a personalized learning experience by understanding the individual student's knowledge, skills, interests, and career goals?EduTwin AI attempts to solve this problem using a combination of:Generative AIPersonal Digital TwinComputer VisionAdaptive LearningAI-generated quizzesSkill-gap analysisCareer guidanceInterview evaluationProposed SolutionEduTwin AI creates a Personal Digital Twin of the student.The student can provide information such as:NameEducationTechnical skillsCoursesProjectsInterestsExperienceCertificationsCareer goalCVThe system processes this information and creates a structured student profile. This profile is then used throughout the application:PlaintextStudent Profile
      │
      ├── Skills
      ├── Courses
      ├── Projects
      ├── Interests
      ├── Experience
      └── Career Goal
             │
             ↓
       Personal Digital Twin
             │
       ┌─────┼────────┐
       ↓     ↓        ↓
  Learning  Quiz    Career
       │     │        │
       ↓     ↓        ↓
   Progress Weak   Roadmap
            Areas
Key Features1. AI Personal Digital TwinEduTwin AI creates a personalized representation of the student including education, technical skills, courses, projects, interests, experience, certifications, and career goals. Information can be entered manually or extracted from a CV.Example:Skills: Python, C++, SQL, Machine Learning, Artificial IntelligenceProjects: AI Course Recommendation System, Carbon Footprint CalculatorCareer Goal: AI Engineer2. AI-Powered CV AnalysisStudents can upload their CV in PDF format. The application workflow runs as follows:PlaintextCV PDF → PyMuPDF → Extracted Text → Groq AI → Structured JSON → Student Profile → Digital Twin
Extracted Information: Name, Education, Skills, Courses, Projects, Interests, Experience, Certifications, and Career Goal.3. Vision TutorEduTwin AI includes a multimodal Vision Tutor for analyzing educational images (machine learning diagrams, neural networks, computer architecture diagrams, flowcharts, graphs, code screenshots, and technical figures).Learning Modes:Understand Mode: Normal technical explanation.Explain Like I'm 5: Simple language and relatable examples.CS Mode: Computer-science-focused technical explanation.Career Mode: Explains utility regarding the student's selected career.4. Adaptive LearningFollows a continuous feedback loop:PlaintextUnderstand → Teach → Test → Evaluate → Detect Weakness → Recommend
5. AI-Generated QuizGenerates targeted quizzes based on skills or manual inputs.Format: 5 questions, 4 options per question, 1 correct answer.Topics: Machine Learning, Python, Artificial Intelligence, Data Structures, Database Systems, Computer Networks, etc.6. Quiz ScoringEvaluated automatically (e.g., 3/5 = 60%) alongside tracking of incorrect responses.7. Weak Topic DetectionQuiz results are categorized by performance levels to generate targeted recommendations:ScorePerformance Level80–100%Strong60–79%Good40–59%Needs PracticeBelow 40%WeakExample Output:Performance: Needs PracticeWeak Topics: Classification, Model EvaluationRecommendation: Review classification algorithms and practice questions on evaluation metrics.Next Learning Step: Study confusion matrix and classification metrics.8. Career GuidanceCompares student skills against requirements for roles like AI Engineer, ML Engineer, Data Scientist, Data Analyst, Software Engineer, Cybersecurity Engineer, or Cloud Engineer.PlaintextCurrent Skills → Career Requirements → Skill Gap Analysis → Missing Skills → Recommended Learning → Career Roadmap
9. AI Interview CoachEvaluates student answers based on performance, technical quality, communication, relevance, career alignment, strengths, and areas for improvement while providing an improved model answer.PlaintextInterview Question → Student Answer → Groq AI → Evaluation → Score + Feedback → Improved Answer
10. Student Progress and RecommendationsConnects all modules into a unified context pipeline:PlaintextCV → Digital Twin → Career Goal → Learning → Quiz → Score → Weak Topics → Recommendation → Next Learning Step
What Makes EduTwin AI Different?EduTwin AI combines Student Context + Generative AI + Vision AI + Assessment + Adaptive Recommendations + Career Guidance.The same learning material yields dynamic explanations depending on the Digital Twin:Student A (Beginner / Data Analyst Goal): Receives basic explanations, simple examples, and data analysis focus.Student B (Advanced / AI Engineer Goal): Receives deep mathematical/algorithmic details and production AI engineering context.High-Level ArchitecturePlaintext                         ┌─────────────────┐
                         │     EDUTWIN     │
                         └────────┬────────┘
                                  │
                  ┌───────────────┴───────────────┐
                  │                               │
                  ▼                               ▼
        ┌──────────────────┐            ┌──────────────────┐
        │  PERSONAL DIGITAL│            │    VISION AI     │
        │       TWIN       │            │                  │
        └────────┬─────────┘            └────────┬─────────┘
                 │                               │
        ┌────────┼────────┐                      │
        │        │        │                      │
        ▼        ▼        ▼                      ▼
       CV     Skills   Career                  Image
                        Goal                     │
        │        │        │                      │
        └────────┴────────┘                      │
                 │                               │
                 └──────────────┬────────────────┘
                                ▼
                       ┌─────────────────┐
                       │     GROQ AI     │
                       │  Qwen 3.6 27B   │
                       └────────┬────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
         Explanation          Quiz            Interview
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                       ┌─────────────────┐
                       │ LEARNING ENGINE │
                       └────────┬────────┘
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
            Progress       Skill Gaps     Recommendations
                │               │                │
                └───────────────┴────────────────┘
                                │
                                ▼
                       Next Learning Step
Adaptive Learning Feedback LoopPlaintext        ┌──────────────────────┐
        │    Student Profile   │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Personalized Learning│
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │       AI Quiz        │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │   Score Performance  │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │   Weak Topic Detect  │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │  AI Recommendation   │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │   Next Learning Step │
        └──────────┬───────────┘
                   │
                   └──────────────→ Student Profile
Technology StackProgramming Language: PythonWeb Application Framework: StreamlitGenerative AI: Groq APIAI Model: qwen/qwen3.6-27bComputer Vision: Multimodal Vision AIPDF Processing: PyMuPDFImage Processing: PillowData Processing: pandasVisualization: PlotlyDatabase: SQLiteVersion Control: GitHubDeployment: Streamlit Community CloudProject StructurePlaintextEduTwin-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── ai/
│   ├── groq_client.py
│   ├── prompts.py
│   ├── cv_analyzer.py
│   └── vision.py
│
├── core/
│   ├── skill_engine.py
│   ├── career_engine.py
│   ├── adaptive_engine.py
│   └── quiz_engine.py
│
├── data/
│   └── careers.json
│
├── database/
│   └── database.py
│
├── utils/
│   └── pdf_parser.py
│
└── pages/
    ├── dashboard.py
    ├── profile.py
    ├── vision_tutor.py
    ├── career.py
    ├── learning.py
    ├── interview.py
    └── quiz.py
Folder Descriptionapp.py: Main entry point and navigation controller.ai/: Handles Groq API interaction (groq_client.py), system prompts (prompts.py), CV parsing (cv_analyzer.py), and vision processing (vision.py).core/: Core business logic for skill processing (skill_engine.py), career comparison (career_engine.py), adaptive recommendations (adaptive_engine.py), and quiz parsing (quiz_engine.py).data/: Application datasets like careers.json.database/: Local storage operations (database.py).utils/: Helper utilities including pdf_parser.py.pages/: Streamlit frontend modules (dashboard.py, profile.py, vision_tutor.py, career.py, learning.py, interview.py, quiz.py).Installation and Setup1. Clone the RepositoryBashgit clone https://github.com/YOUR-USERNAME/EduTwin-AI.git
cd EduTwin-AI
2. Install DependenciesBashpip install -r requirements.txt
3. Configure Groq API KeySet your environment key or add it to Streamlit Secrets:Ini, TOMLGROQ_API_KEY = "your_api_key_here"
Important: Never commit API keys to version control. Keep .env and .streamlit/secrets.toml listed in .gitignore.Running the ApplicationBashstreamlit run app.py
Deployment on Streamlit Community CloudPush code to GitHub.Log into Streamlit Community Cloud and select the repository.Set the Main File Path to app.py.Add GROQ_API_KEY under Secrets.Click Deploy.TestingTest 1 (CV Upload): Confirm PDF extraction and structured profile output.Test 2 (Digital Twin): Verify skills, projects, and goals populate correctly.Test 3 (Learning): Confirm topic-based AI text generation.Test 4 (Quiz): Verify generation of 5 MCQs and scoring logic.Test 5 (Score Tiering): Test score outputs (100% Strong, 60% Good, 40% Practice, 20% Weak).Test 6 (Vision Tutor): Test diagram explanations across all 4 learning modes.Test 7 (Interview Coach): Check evaluation, scoring, and sample answer output.Example Student WorkflowPlaintext1. Upload CV → 2. AI Analyzes CV → 3. Create Digital Twin → 4. View Dashboard 
   → 5. Select Career → 6. Identify Skill Gaps → 7. Study Topic 
   → 8. Upload Diagram to Vision Tutor → 9. Take Quiz → 10. Receive Score 
   → 11. Detect Weak Topics → 12. Receive Recommendations → 13. Practice Interview
Example Use CaseFor a BS Computer Science student aiming to be an AI Engineer:Learning: System targets machine learning topics tailored to existing Python/C++ skills.Vision Tutor: Explains an uploaded neural network diagram tailored to AI Engineering.Quiz & Evaluation: Identifies model evaluation weak points from quiz failures.Recommendation: Directs student to study Confusion Matrix, Precision, Recall, and F1 Score next.AI Prompt DesignAll system prompts reside separately in ai/prompts.py (CV Analysis, Learning, Interview, Quiz Generation, and Quiz Analysis) to maintain clean separation of concerns.AI Response ProcessingStructured outputs are parsed and validated via JSON schemas:JSON{
  "questions": [
    {
      "question": "What is supervised learning?",
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "answer": 1
    }
  ]
}
Functional ModulesModuleMain FunctionDigital TwinCreates and stores student profileCV AnalyzerExtracts and structures CV informationVision TutorExplains educational images and diagramsLearningGenerates personalized learning modulesQuizGenerates and evaluates knowledge quizzesAdaptive EngineIdentifies knowledge gaps and weak areasCareer EngineHandles career mapping and skill-gap analysisInterview CoachEvaluates practice interview responsesDashboardDisplays student context and learning metricsProject ObjectivesCreate a personalized Digital Twin for every student.Deliver tailored learning content via Generative AI.Provide multimodal explanations for diagrams/images.Assess understanding with automated AI quizzes.Identify weak topics dynamically.Recommend precise next learning steps.Support career exploration and gap analysis.Provide interactive interview preparation.Future EnhancementsLong-Term Memory: Persistent tracking of performance metrics across sessions.Advanced Analytics: Dynamic charts tracking skill growth over time.Automated Learning Paths: Multi-stage sequential roadmaps (e.g., Python → NumPy → ML → Deep Learning).Career Simulations: Comparative analysis between alternative career goals.Voice Tutor: Real-time conversational audio interface.Extended Multimodality: Support for educational video, audio, and handwritten notes.LimitationsAI Accuracy: Output standard depends on LLM generative constraints; responses may occasionally require verification.API Dependencies: Operations rely on external Groq API availability.CV Extraction Quality: Parsing accuracy varies with complex non-standard PDF formats.Vision Complexity: Detailed technical diagrams require high-resolution source images.TeamMaryam KhanMuhammad Shahzeb KhanMuhammad Zaid KhanMuhammad Zain KhanProject Development ProcessPlaintextIdea Generation → Problem Identification → Solution Design → Requirement Analysis 
  → System Architecture → Streamlit Development → Groq AI Integration 
  → Module Development → Testing → GitHub & Streamlit Deployment
Development PhilosophyPersonalization: Understand the student before teaching.Adaptability: Use performance metrics to drive future learning direction.Multimodal Learning: Combine visual, technical, and textual education.Core EduTwin ConceptPlaintext┌─────────────────┐
│    UNDERSTAND   │
│  Student Profile│
└────────┬────────┘
         ↓
┌─────────────────┐
│      TEACH      │
│ Personalized AI │
└────────┬────────┘
         ↓
┌─────────────────┐
│      TEST       │
│     AI Quiz     │
└────────┬────────┘
         ↓
┌─────────────────┐
│    EVALUATE     │
│ Score & Feedback│
└────────┬────────┘
         ↓
┌─────────────────┐
│      ADAPT      │
│   Weak Topics   │
└────────┬────────┘
         ↓
┌─────────────────┐
│    RECOMMEND    │
│    Next Step    │
└────────┬────────┘
         │
         └──────────→ (Loop back to TEACH)
Key InnovationEduTwin AI transforms standard LLM interactions into an adaptive educational ecosystem by answering:Who is the student?What do they already know?What is their career objective?What are their current weak points?What should they study next?ConclusionEduTwin AI shifts education away from static content by establishing a continuous Understand → Teach → Test → Evaluate → Adapt → Recommend cycle, proving how Generative AI can power an end-to-end personalized learning engine.
