import streamlit as st

from ai.vision import analyze_image
from utils.style import load_css


st.set_page_config(
    page_title="EduTwin - Vision Tutor",
    page_icon="📷",
    layout="wide"
)


load_css()


# =========================================
# HERO
# =========================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-small">
            MULTIMODAL AI LEARNING
        </div>

        <div class="hero-title">
            Show me what you're learning. 📷
        </div>

        <div class="hero-text">
            Upload a diagram, graph, computer component,
            code screenshot or educational image.
            EduTwin will explain it according to your
            knowledge and career goal.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================
# CHECK PROFILE
# =========================================

if "profile" not in st.session_state:

    st.warning(
        "Please create your Digital Twin profile first."
    )

    if st.button(
        "👤 Create My Profile",
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )

    st.stop()


profile = st.session_state["profile"]


# =========================================
# UPLOAD
# =========================================

st.markdown(
    '<div class="section-label">STEP 01</div>',
    unsafe_allow_html=True
)

st.subheader(
    "📸 Upload something you want to understand"
)


uploaded_image = st.file_uploader(
    "Choose an educational image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
)


# =========================================
# EXPLANATION MODE
# =========================================

st.markdown(
    '<div class="section-label">STEP 02</div>',
    unsafe_allow_html=True
)

st.subheader(
    "🧠 Choose how EduTwin should teach you"
)


mode = st.selectbox(
    "Explanation mode",
    [
        "Understand",
        "Explain Like I'm 5",
        "CS Mode",
        "Career Mode"
    ]
)


# =========================================
# DISPLAY IMAGE
# =========================================

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Image",
        use_container_width=True
    )


    st.write("")


    # =====================================
    # ANALYZE BUTTON
    # =====================================

    if st.button(
        "🧠 Analyze Image",
        type="primary",
        use_container_width=False
    ):

        try:

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            image_bytes = (
                uploaded_image.getvalue()
            )


            prompt = f"""
You are EduTwin AI, a personalized visual tutor.

Student information:

Name:
{profile["name"]}

Education:
{profile["education"]}

Skills:
{profile["skills"]}

Career goal:
{profile["career_goal"]}

Selected explanation mode:
{mode}

Analyze the uploaded image.

First identify what is visible.

Then explain it according to the selected mode.

If the image contains a:

- computer component
- diagram
- graph
- chart
- programming concept
- mathematical concept
- technical object
- educational material

explain its purpose and the most important concepts.

Connect the explanation to the student's
knowledge and career goal where appropriate.

Do not invent details that cannot be observed.

Use simple language.

Keep the response concise.

Use headings and bullet points where useful.

Keep the answer below 400 words.
"""


            # =================================
            # AI ANALYSIS
            # =================================

            with st.spinner(
                "🔍 EduTwin is analyzing your image..."
            ):

                answer = analyze_image(
                    st.secrets["GROQ_API_KEY"],
                    image_bytes,
                    prompt
                )


            st.success(
                "✅ Image analysis completed!"
            )


            st.markdown(
                '<div class="section-label">AI RESULT</div>',
                unsafe_allow_html=True
            )

            st.subheader(
                "🧠 Your Personalized Explanation"
            )


            st.markdown(
                answer
            )


        except Exception as error:

            st.error(
                f"Vision AI error: {error}"
            )
