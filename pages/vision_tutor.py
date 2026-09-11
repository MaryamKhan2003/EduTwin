import streamlit as st

from ai.vision import analyze_image


st.set_page_config(
    page_title="EduTwin - Vision Tutor",
    page_icon="📷",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "📷 Vision Tutor"
)

st.subheader(
    "Show me what you're learning."
)

st.write(
    """
    Upload a diagram, graph, computer component,
    code screenshot or educational image.

    EduTwin will explain it according to your
    knowledge and career goal.
    """
)

st.divider()


# ============================================================
# PROFILE CHECK
# ============================================================

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


# ============================================================
# STUDENT INFORMATION
# ============================================================

with st.expander(
    "👤 Your current Digital Twin",
    expanded=False
):

    st.write(
        f"**Education:** {profile['education']}"
    )

    st.write(
        f"**Skills:** {profile['skills']}"
    )

    st.write(
        f"**Career Goal:** {profile['career_goal']}"
    )


# ============================================================
# IMAGE UPLOAD
# ============================================================

st.header(
    "📸 Step 1 — Upload an Image"
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


# ============================================================
# EXPLANATION MODE
# ============================================================

st.header(
    "🧠 Step 2 — Choose Explanation Mode"
)


mode = st.selectbox(
    "How should EduTwin explain it?",
    [
        "Understand",
        "Explain Like I'm 5",
        "CS Mode",
        "Career Mode"
    ]
)


# ============================================================
# IMAGE PREVIEW
# ============================================================

if uploaded_image is not None:

    st.header(
        "👀 Image Preview"
    )

    st.image(
        uploaded_image,
        caption="Your uploaded image",
        use_container_width=True
    )


    st.divider()


    # ========================================================
    # ANALYZE
    # ========================================================

    if st.button(
        "🧠 Analyze Image",
        type="primary"
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

If the image contains:

- a computer component
- a diagram
- a graph
- a chart
- programming code
- a mathematical concept
- a technical object
- educational material

explain its purpose and important concepts.

Connect the explanation to the student's
knowledge and career goal when appropriate.

Do not invent details that cannot be observed.

Use simple language.

Use headings and bullet points where useful.

Keep the response below 400 words.
"""


            # =================================================
            # AI REQUEST
            # =================================================

            with st.spinner(
                "🔍 EduTwin is analyzing your image..."
            ):

                answer = analyze_image(
                    st.secrets["GROQ_API_KEY"],
                    image_bytes,
                    prompt
                )


            st.success(
                "✅ Analysis completed!"
            )


            st.header(
                "🧠 Your Personalized Explanation"
            )


            st.markdown(
                answer
            )


        except Exception as error:

            st.error(
                f"Vision AI error: {error}"
            )


else:

    st.info(
        "📷 Upload an image above to start learning."
    )
