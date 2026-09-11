import streamlit as st
from utils.style import load_css
from ai.vision import analyze_image


st.set_page_config(
    page_title="EduTwin - Vision Tutor",
    page_icon="📷",
    layout="wide"
)
load_css()

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

st.markdown(
    '<div class="section-label">STEP 01</div>',
    unsafe_allow_html=True
)

st.subheader(
    "📸 Upload something you want to understand"
)

st.write(
    """
    Upload an educational image and EduTwin will identify
    what you are looking at and explain it according to
    your Digital Twin.
    """
)


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


uploaded_image = st.file_uploader(
    "Upload an educational image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
)
st.markdown(
    '<div class="section-label">STEP 02</div>',
    unsafe_allow_html=True
)

st.subheader(
    "🧠 Choose how EduTwin should teach you"
)


mode = st.selectbox(
    "Choose explanation mode",
    [
        "Understand",
        "Explain Like I'm 5",
        "CS Mode",
        "Career Mode"
    ]
)


if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Image",
        use_container_width=True
    )


    if st.button(
        "🧠 Analyze Image",
        type="primary"
    ):

        try:

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from Streamlit Secrets."
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

If the image contains:

- a diagram
- computer component
- programming code
- graph
- chart
- mathematical concept
- technical object
- educational material

explain its purpose and important concepts.

Connect the explanation to the student's
current knowledge and career goal where appropriate.

Do not invent details that cannot be observed.

Use simple educational language.
"""


            with st.spinner(
                "Vision AI is analyzing the image..."
            ):

                answer = analyze_image(
                    st.secrets["GROQ_API_KEY"],
                    image_bytes,
                    prompt
                )


            st.success(
                "✅ Image analysis completed!"
            )


            st.subheader(
                "🧠 AI Explanation"
            )


            st.markdown(
                answer
            )


        except Exception as error:

            st.error(
                f"Vision AI error: {error}"
            )
