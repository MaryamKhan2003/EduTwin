#  EduTwin AI

## An AI-Powered Personal Digital Twin for Adaptive Multimodal Learning and Career Development

EduTwin AI is an AI-powered educational platform that creates a **Personal Digital Twin of a student** based on their skills, education, courses, projects, interests, experience, and career goals.

Instead of providing the same learning experience to every student, EduTwin AI first tries to understand **who the student is, what they already know, what they want to achieve, and where they have knowledge gaps**.

The system then uses Generative AI to provide personalized learning, visual explanations, quizzes, weak-topic detection, career guidance, and interview practice.

> **EduTwin AI doesn't just teach the student. It first understands the student, then teaches, tests, evaluates, and recommends what to learn next.**

---

#  Project Overview

Traditional learning systems often follow a **one-size-fits-all approach**.

Every student may receive:

- The same learning material
- The same explanations
- The same difficulty level
- The same quiz questions
- The same learning path

However, students have different:

- Knowledge levels
- Technical skills
- Interests
- Academic backgrounds
- Career goals
- Learning difficulties

EduTwin AI addresses this problem by creating a **student-specific Digital Twin**.

The Digital Twin becomes the foundation for personalized AI interactions.

### Basic Concept

```text
Student Information
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

 Problem Statement

Students often struggle to identify:

What skills they already have
Which skills are missing for their desired career
Which topics they are weak in
What they should learn next
How to understand complex technical diagrams and concepts
Whether they are actually improving
How prepared they are for interviews

Most educational platforms provide general content without considering the student's complete profile.

The main problem is:

How can AI provide a personalized learning experience by understanding the individual student's knowledge, skills, interests, and career goals?

EduTwin AI attempts to solve this problem using a combination of:

Generative AI
Personal Digital Twin
Computer Vision
Adaptive Learning
AI-generated quizzes
Skill-gap analysis
Career guidance
Interview evaluation
 Proposed Solution

EduTwin AI creates a Personal Digital Twin of the student.

The student can provide information such as:

Name
Education
Technical skills
Courses
Projects
Interests
Experience
Certifications
Career goal
CV

The system processes this information and creates a structured student profile.

This profile is then used throughout the application.

For example:

Student Profile
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
       ┌──────┼────────┐
       ↓      ↓        ↓
   Learning  Quiz    Career
       │      │        │
       ↓      ↓        ↓
    Progress Weak     Roadmap
             Areas
 Key Features
1.  AI Personal Digital Twin

EduTwin AI creates a personalized representation of the student.

The profile can include:

Education
Technical skills
Courses
Projects
Interests
Experience
Certifications
Career goal

The information can be entered manually or extracted from a CV.

Example
Skills:
Python
C++
SQL
Machine Learning
Artificial Intelligence

Projects:
AI Course Recommendation System
Carbon Footprint Calculator

Career Goal:
AI Engineer

The information becomes the foundation for personalized AI recommendations.

2.  AI-Powered CV Analysis

Students can upload their CV in PDF format.

The application:

Reads the PDF
Extracts text
Sends relevant information to Groq AI
Identifies student information
Generates a structured profile
Provides AI-based analysis

The extracted information may include:

Name
Education
Skills
Courses
Projects
Interests
Experience
Certifications
Career goal
CV Workflow
CV PDF
  ↓
PyMuPDF
  ↓
Extracted Text
  ↓
Groq AI
  ↓
Structured JSON
  ↓
Student Profile
  ↓
Digital Twin
3.  Vision Tutor

EduTwin AI includes a multimodal Vision Tutor.

Students can upload educational images such as:

Machine learning diagrams
Neural network diagrams
Computer architecture diagrams
Flowcharts
Graphs
Code screenshots
Technical components
Educational figures

The Vision AI analyzes the uploaded image and provides an explanation.

The explanation can be personalized according to the student's profile.

Learning Modes

The system can support different explanation styles such as:

 Understand Mode

Provides a normal technical explanation.

 Explain Like I'm 5

Explains the concept using very simple language and examples.

 CS Mode

Provides a computer-science-focused explanation.

 Career Mode

Explains why the concept may be useful for the student's selected career.

4.  Adaptive Learning

EduTwin AI attempts to make learning adaptive rather than static.

Instead of simply showing information, the system follows:

Understand
    ↓
Teach
    ↓
Test
    ↓
Evaluate
    ↓
Detect Weakness
    ↓
Recommend

This creates a feedback loop.

The student's performance can influence what they should study next.

5.  AI-Generated Quiz

The Quiz module generates a quiz using Generative AI.

Each quiz contains:

5 questions
4 options per question
One correct answer

The topic can be selected from the student's skills/courses or entered manually.

Example topics:

Machine Learning
Python
Artificial Intelligence
Data Structures
Database Systems
Computer Networks
6.  Quiz Scoring

Quiz answers are evaluated automatically.

For example:

Correct Answers: 3
Total Questions: 5

Score:
3 / 5 = 60%

The system also identifies the questions that were answered incorrectly.

7.  Weak Topic Detection

The quiz result is sent to the AI analysis system.

Based on the performance, the system identifies possible weak areas.

Performance levels include:

Score	Performance
80–100%	Strong
60–79%	Good
40–59%	Needs Practice
Below 40%	Weak

The system can then generate:

Weak topics
Personalized recommendations
Next learning step

Example:

Performance:
Needs Practice

Weak Topics:
- Classification
- Model Evaluation

Recommendation:
Review classification algorithms and practice
more questions involving evaluation metrics.

Next Learning Step:
Study confusion matrix and classification metrics.
8.  Career Guidance

EduTwin AI can help students explore career paths based on their profile.

Possible career options include:

AI Engineer
Machine Learning Engineer
Data Scientist
Data Analyst
Software Engineer
Cybersecurity Engineer
Cloud Engineer
Other

The system can compare the student's existing skills with career requirements.

Example
Current Skills
      ↓
Career Requirements
      ↓
Skill Gap Analysis
      ↓
Missing Skills
      ↓
Recommended Learning
      ↓
Career Roadmap
9.  AI Interview Coach

EduTwin AI includes an AI-powered interview practice system.

The student answers an interview question.

The AI evaluates the response based on factors such as:

Overall performance
Technical quality
Communication
Relevance
Career alignment
Strengths
Areas for improvement

The system can also provide an improved example answer.

Interview Workflow
Interview Question
       ↓
Student Answer
       ↓
Groq AI
       ↓
Evaluation
       ↓
Score + Feedback
       ↓
Improved Answer
10.  Student Progress and Recommendations

EduTwin AI connects different modules instead of treating them as completely separate tools.

For example:

CV
 ↓
Digital Twin
 ↓
Career Goal
 ↓
Learning
 ↓
Quiz
 ↓
Score
 ↓
Weak Topics
 ↓
Recommendation
 ↓
Next Learning Step

This feedback loop is one of the main concepts behind EduTwin AI.

 What Makes EduTwin AI Different?

The main idea is not simply using an LLM to answer questions.

The system combines:

Student Context
      +
Generative AI
      +
Vision AI
      +
Assessment
      +
Adaptive Recommendations
      +
Career Guidance

The key concept is personalization.

For example, if two students upload the same machine-learning diagram:

Student A
Beginner
Career Goal: Data Analyst

The system can provide:

Basic explanation
Simple examples
Data-analysis relevance
Student B
Advanced
Career Goal: AI Engineer

The system can provide:

More technical explanation
Mathematical/algorithmic details
AI engineering relevance

Therefore:

The same learning material can produce different explanations depending on the student's Digital Twin.

 High-Level Architecture
                         ┌─────────────────┐
                         │     EDUTWIN     │
                         └────────┬────────┘
                                  │
                 ┌────────────────┴────────────────┐
                 │                                 │
                 ▼                                 ▼
        ┌──────────────────┐             ┌──────────────────┐
        │  PERSONAL DIGITAL│             │    VISION AI     │
        │       TWIN       │             │                  │
        └────────┬─────────┘             └────────┬─────────┘
                 │                                │
        ┌────────┼────────┐                       │
        │        │        │                       │
        ▼        ▼        ▼                       ▼
       CV      Skills   Career                  Image
                         Goal
        │        │        │                       │
        └────────┴────────┘                       │
                 │                                │
                 └──────────────┬─────────────────┘
                                ▼
                       ┌─────────────────┐
                       │     GROQ AI     │
                       │   Qwen 3.6 27B │
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
                       │ LEARNING ENGINE│
                       └────────┬────────┘
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
            Progress       Skill Gaps       Recommendations
                │               │                │
                └───────────────┴────────────────┘
                                │
                                ▼
                        Next Learning Step
 Adaptive Learning Feedback Loop

One of the central concepts of EduTwin AI is the feedback loop.

        ┌──────────────────────┐
        │   Student Profile    │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Personalized Learning│
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │      AI Quiz         │
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
        │ AI Recommendation    │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │   Next Learning Step │
        └──────────┬───────────┘
                   │
                   └──────────────→ Student Profile
 Technology Stack
Programming Language
Python

Python is used as the primary programming language for:

Application development
AI integration
Data processing
Quiz generation
Profile analysis
Business logic
Web Application Framework
Streamlit

Streamlit is used to build the interactive web application.

It provides:

User interface
Navigation
Forms
File upload
Buttons
Session state
Interactive components
Generative AI
Groq API

Groq API is used for AI-powered functionality including:

CV analysis
Personalized learning
Quiz generation
Quiz analysis
Interview evaluation
Recommendations
AI Model

The application uses:

qwen/qwen3.6-27b

for text and multimodal AI tasks.

Computer Vision

The Vision Tutor uses a multimodal AI model to process:

Images
Diagrams
Graphs
Screenshots
Technical figures
PDF Processing
PyMuPDF

PyMuPDF is used to extract text from uploaded PDF CV files.

Image Processing
Pillow

Pillow is used for image handling and processing.

Data Processing
pandas

Pandas can be used for structured data handling and analysis.

Visualization
Plotly

Plotly is used for interactive visualizations where required.

Database
SQLite

SQLite provides lightweight local database support for application-related data.

Version Control
GitHub

GitHub is used for:

Source code management
Version control
Project collaboration
Repository hosting
Deployment
Streamlit Community Cloud

The application is deployed using Streamlit Community Cloud.

 Project Structure
EduTwin-AI/
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
 Folder Description
app.py

Main entry point of the Streamlit application.

It controls the main application interface and navigation.

ai/

Contains AI-related functionality.

groq_client.py

Handles communication with the Groq API.

Responsible for:

Groq client creation
Text generation
JSON generation
API key handling
prompts.py

Contains prompts used by the AI modules.

Prompts are separated from application logic to make them easier to maintain.

cv_analyzer.py

Processes AI-generated CV analysis and converts it into structured profile information.

vision.py

Handles multimodal image analysis.

It prepares images and sends them to the Vision AI model.

core/

Contains the main application logic.

skill_engine.py

Handles skill-related processing.

career_engine.py

Handles career comparison and career-related logic.

adaptive_engine.py

Handles adaptive learning and recommendations.

quiz_engine.py

Handles:

Quiz generation
Answer checking
Score calculation
Weak-topic analysis
AI recommendations
data/

Contains application data.

careers.json

Stores career-related information used by the application.

database/

Contains database-related functionality.

database.py

Handles SQLite-related operations.

utils/

Contains helper functions.

pdf_parser.py

Extracts text from PDF documents.

pages/

Contains the main Streamlit application pages.

dashboard.py

Displays the student's overall Digital Twin information and progress.

profile.py

Handles:

CV upload
CV analysis
Profile creation
Digital Twin creation
vision_tutor.py

Provides multimodal visual learning.

career.py

Provides career exploration and skill-gap analysis.

learning.py

Provides personalized learning content.

interview.py

Provides AI interview practice and evaluation.

quiz.py

Provides AI-generated quizzes and performance analysis.

 Installation and Setup
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/EduTwin-AI.git

Move into the project directory:

cd EduTwin-AI
2. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

The project uses:

streamlit
groq
pymupdf
pillow
pandas
plotly
3. Configure Groq API Key

EduTwin AI requires a Groq API key.

For local development, the application expects the key as:

GROQ_API_KEY

For Streamlit Community Cloud, add the key through the application's Secrets configuration.

Example:

GROQ_API_KEY = "your_api_key_here"
Important

Do not commit your API key to GitHub.

Never place the actual API key inside:

app.py
groq_client.py
README.md

or any other source file.

 Running the Application

Start Streamlit with:

streamlit run app.py

The application will open in the browser.

 Deployment on Streamlit Community Cloud

EduTwin AI can be deployed using Streamlit Community Cloud.

Step 1 — Push Project to GitHub

Upload the complete project structure to GitHub.

Make sure the repository contains:

app.py
requirements.txt
README.md
ai/
core/
data/
database/
utils/
pages/
.streamlit/
Step 2 — Open Streamlit Community Cloud

Create a new application and select the EduTwin AI GitHub repository.

Step 3 — Select Main File

Set the main application file to:

app.py
Step 4 — Add Secrets

Open the application's secrets/settings area and add:

GROQ_API_KEY = "your_api_key_here"
Step 5 — Deploy

Deploy the application.

Streamlit Community Cloud installs the dependencies from:

requirements.txt

and starts the application using:

app.py
 Security

EduTwin AI uses environment/application secrets for the Groq API key.

The API key should never be stored directly in the GitHub repository.

The .gitignore file includes:

.streamlit/secrets.toml
.env

This helps prevent accidental API-key commits during local development.

 Testing

The application should be tested module by module.

Test 1 — CV Upload

Upload a valid PDF CV.

Expected result:

CV
 ↓
Text Extraction
 ↓
AI Analysis
 ↓
Structured Profile
Test 2 — Digital Twin

After CV analysis, verify that fields such as:

Skills
Courses
Projects
Interests
Career goal

are correctly populated.

Test 3 — Learning

Select a learning topic.

Verify that AI-generated learning content is produced.

Test 4 — Quiz

Generate a quiz.

Expected:

5 Questions
4 Options Each

Answer all five questions.

Verify:

Score
Percentage
Performance level
Incorrect questions
Weak topics
Recommendation
Next learning step
Test 5 — Different Quiz Scores

The quiz should be tested with different performance levels.

Example
5/5 → 100% → Strong

3/5 → 60% → Good

2/5 → 40% → Needs Practice

1/5 → 20% → Weak
Test 6 — Vision Tutor

Upload an educational image.

Test different explanation modes:

Understand
Explain Like I'm 5
CS Mode
Career Mode
Test 7 — Interview

Answer an interview question.

Verify that the system generates:

Score
Technical evaluation
Communication feedback
Relevance
Career alignment
Strengths
Improvements
Better answer
 Example Student Workflow

A typical student interaction can look like this:

1. Upload CV
        ↓
2. AI analyzes CV
        ↓
3. Create Digital Twin
        ↓
4. View Dashboard
        ↓
5. Select Career
        ↓
6. Identify Skill Gaps
        ↓
7. Study a Topic
        ↓
8. Upload Diagram to Vision Tutor
        ↓
9. Take AI Quiz
        ↓
10. Receive Score
        ↓
11. Detect Weak Topics
        ↓
12. Receive AI Recommendation
        ↓
13. Continue Learning
        ↓
14. Practice Interview
 Example Use Case

Consider a Computer Science student whose profile contains:

Education:
BS Computer Science

Skills:
Python
C++
Machine Learning
SQL

Projects:
AI Course Recommendation System

Interests:
Artificial Intelligence
Machine Learning

Career Goal:
AI Engineer

EduTwin AI can use this information to personalize the student's experience.

For example:

Learning

The system can recommend machine-learning topics relevant to the student's current skills.

Vision Tutor

If the student uploads a neural-network diagram, the system can explain it according to their knowledge and AI career goal.

Quiz

The system can generate five machine-learning questions.

Performance

If the student performs poorly in model evaluation, the system can identify it as a weak area.

Recommendation

The system can recommend:

Review:
Model Evaluation

Next:
Confusion Matrix
Precision
Recall
F1 Score

This creates a continuous learning cycle.

 AI Prompt Design

EduTwin AI separates AI prompts from application logic.

Prompts are stored in:

ai/prompts.py

Different prompts are used for different tasks.

Examples include:

CV Analysis Prompt
Learning Prompt
Interview Prompt
Quiz Generation Prompt
Quiz Analysis Prompt

This approach makes the application easier to:

Maintain
Debug
Improve
Customize
 AI Response Processing

For structured AI tasks, the application uses JSON-based responses.

For example, a quiz response can follow this structure:

{
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

The application then validates the generated information before using it.

 Functional Modules
Module	Main Function
Digital Twin	Creates student profile
CV Analyzer	Extracts and analyzes CV information
Vision Tutor	Explains educational images
Learning	Generates personalized learning
Quiz	Generates and evaluates quizzes
Adaptive Engine	Detects learning weaknesses
Career Engine	Supports career exploration
Interview Coach	Evaluates interview answers
Dashboard	Presents student information and progress
 Project Objectives

The major objectives of EduTwin AI are:

Objective 1

Create a personalized Digital Twin representing a student's educational and career profile.

Objective 2

Use Generative AI to provide personalized learning content.

Objective 3

Use multimodal AI to explain educational images and diagrams.

Objective 4

Evaluate student understanding through AI-generated quizzes.

Objective 5

Detect weak topics based on quiz performance.

Objective 6

Recommend appropriate next learning steps.

Objective 7

Support students in exploring career paths and skill gaps.

Objective 8

Provide AI-powered interview practice.

 Future Enhancements

EduTwin AI can be extended in several ways.

1. Long-Term Student Memory

Store learning history and previous performance to create a more persistent Digital Twin.

2. Advanced Progress Tracking

Track:

Quiz scores
Topics completed
Weak areas
Learning time
Improvement over time
3. Personalized Learning Paths

Automatically create complete learning paths such as:

Python
 ↓
NumPy
 ↓
Pandas
 ↓
Machine Learning
 ↓
Deep Learning
 ↓
AI Projects
4. More Career Simulations

Students could simulate different career choices.

For example:

AI Engineer
vs
Data Scientist
vs
Software Engineer

The system could compare:

Existing skills
Missing skills
Recommended courses
Project requirements
Career readiness
5. Voice-Based Tutor

A future version could allow students to interact with EduTwin using voice.

6. Learning Analytics

Future versions could include detailed analytics dashboards showing:

Skill Growth
Quiz Performance
Weak Areas
Learning Progress
Career Readiness
7. More Multimodal Learning

The Vision Tutor could be expanded to support:

Educational videos
Audio explanations
Handwritten notes
Screenshots
Presentations
Interactive diagrams
 Limitations

EduTwin AI is a prototype educational system and has several limitations.

AI Accuracy

Generative AI responses may sometimes contain inaccurate or incomplete information.

API Dependency

AI features depend on the availability and limits of the Groq API.

CV Quality

CV analysis depends on the quality and structure of the uploaded document.

Vision Analysis

Image explanations depend on image quality and the complexity of the visual content.

Personalized Recommendations

Recommendations are AI-generated and should be considered guidance rather than guaranteed career advice.

 Team
Team Members
Maryam Khan
Muhammad Shahzeb Khan
Muhammad Zaid Khan
Muhammad Zain Khan



Add additional team members here if your final project team contains more members.

 Project Development Process

The project was developed through the following stages:

Idea Generation
      ↓
Problem Identification
      ↓
Solution Design
      ↓
Requirement Analysis
      ↓
System Architecture
      ↓
Streamlit Development
      ↓
Groq AI Integration
      ↓
CV Analysis
      ↓
Vision Tutor
      ↓
Adaptive Learning
      ↓
Quiz System
      ↓
Career Guidance
      ↓
Interview Coach
      ↓
Testing
      ↓
GitHub
      ↓
Streamlit Cloud Deployment
 Development Philosophy

EduTwin AI was designed around three major principles:

1. Personalization

The system should understand the student before generating learning content.

2. Adaptability

The system should use performance information to recommend what the student should learn next.

3. Multimodal Learning

Students should be able to learn not only through text but also through visual educational material.

 Core EduTwin Concept

The entire project can be summarized by this loop:

              ┌─────────────────┐
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
              │    AI Quiz      │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │     EVALUATE    │
              │ Score & Feedback│
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │     ADAPT       │
              │ Weak Topics     │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │   RECOMMEND     │
              │ Next Step       │
              └────────┬────────┘
                       │
                       └──────────→ TEACH
 Key Innovation

The key innovation of EduTwin AI is the combination of a Personal Digital Twin + Multimodal Generative AI + Adaptive Assessment.

Most AI tutors focus on answering the current question.

EduTwin AI focuses on the student's overall learning journey.

The system attempts to answer:

Who is the student?

What does the student already know?

What is the student trying to become?

What does the student need to learn?

What is the student struggling with?

What should the student learn next?

 Conclusion

EduTwin AI is an AI-powered personalized learning platform designed to move beyond traditional one-size-fits-all education.

By creating a Personal Digital Twin, the system can use student-specific information to support:

Personalized learning
Multimodal visual education
AI-generated quizzes
Weak-topic detection
Adaptive recommendations
Career exploration
Skill-gap analysis
Interview preparation

The central idea is simple:

Understand → Teach → Test → Evaluate → Adapt → Recommend

EduTwin AI aims to demonstrate how Generative AI can be used not just as a chatbot, but as part of a complete personalized educational ecosystem.
