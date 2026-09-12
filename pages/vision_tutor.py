import streamlit as st

from ai.vision import analyze_image


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="EduTwin - Vision Tutor",
    page_icon="📷",
    layout="wide"
)


# ==================================================
# PROFILE CHECK
# ==================================================

if "profile" not in st.session_state:

    st.title(
        "📷 Vision Tutor"
    )

    st.warning(
        "Create your Digital Twin first."
    )

    if st.button(
        " Create My Digital Twin",
        type="primary"
    ):

        st.switch_page(
            "pages/profile.py"
        )

    st.stop()


profile = st.session_state["profile"]


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title(
        " Vision Tutor"
    )

    st.caption(
        "AI-powered visual learning"
    )

    st.divider()

    st.write(
        f" **{profile['name']}**"
    )

    st.write(
        f" {profile['career_goal']}"
    )

    st.divider()

    st.info(
        """
        Upload something you're learning.

        EduTwin will explain what you see
        according to your profile.
        """
    )


# ==================================================
# HEADER
# ==================================================

st.title(
    " Vision Tutor"
)

st.subheader(
    "Show me what you're learning."
)

st.write(
    """
    Upload a diagram, graph, code screenshot,
    computer component or educational image.
    """
)

st.divider()


# ==================================================
# DIGITAL TWIN
# ==================================================

with st.expander(
    " View your Digital Twin",
    expanded=False
):

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Education:** {profile['education']}"
        )

        st.write(
            f"**Skills:** {profile['skills']}"
        )

    with col2:

        st.write(
            f"**Career:** {profile['career_goal']}"
        )

        st.write(
            f"**Interests:** {profile['interests']}"
        )


# ==================================================
# STEP 1
# ==================================================

st.header(
    " Step 1 — Upload Your Learning Material"
)

uploaded_image = st.file_uploader(
    "Choose an image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ],
    help=(
        "Try a diagram, graph, chart, "
        "code screenshot or technical object."
    )
)


# ==================================================
# STEP 2
# ==================================================

st.header(
    " Step 2 — Choose Explanation Mode"
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


# ==================================================
# STEP 3
# ==================================================

if uploaded_image is not None:

    st.divider()

    st.header(
        " Step 3 — Preview"
    )

    st.image(
        uploaded_image,
        caption="Your learning material",
        use_container_width=True
    )

    st.write("")

    if st.button(
        " Analyze With EduTwin AI",
        type="primary",
        use_container_width=True
    ):

        try:

            if "GROQ_API_KEY" not in st.secrets:

                st.error(
                    "GROQ_API_KEY is missing from "
                    "Streamlit Secrets."
                )

                st.stop()


            image_bytes = uploaded_image.getvalue()


            prompt = f"""
You are EduTwin AI, a personalized visual tutor.

Student name:
{profile["name"]}

Education:
{profile["education"]}

Skills:
{profile["skills"]}

Career goal:
{profile["career_goal"]}

Interests:
{profile["interests"]}

Explanation mode:
{mode}

Analyze the uploaded image.

First identify what is visible.

Then explain it according to the selected mode.

If it contains a computer component, diagram,
graph, chart, programming code, mathematical
concept, technical object or educational material,
explain its purpose and important concepts.

Connect the explanation to the student's
knowledge and career goal when useful.

Do not invent details that cannot be observed.

Use simple language.

Use headings and bullet points.

Keep the response below 400 words.
"""


            with st.spinner(
                " EduTwin is analyzing your image..."
            ):

                answer = analyze_image(
                    st.secrets["GROQ_API_KEY"],
                    image_bytes,
                    prompt
                )


            st.success(
                " Analysis completed!"
            )

            st.divider()

            st.header(
                " Your Personalized Explanation"
            )

            st.markdown(
                answer
            )


        except Exception as error:

            st.error(
                f" Vision AI error: {error}"
            )

else:

    st.info(
        """
         **Your visual tutor is ready.**

        Upload an image above to begin.
        """
    )
