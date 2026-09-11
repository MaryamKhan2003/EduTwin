import base64

import streamlit as st

from groq import Groq


st.set_page_config(
    page_title="EduTwin - Vision Tutor",
    page_icon="📷",
    layout="wide"
)


st.title("📷 AI Vision Tutor")


st.write(
    """
    Upload an educational image and EduTwin will identify
    and explain what you are looking at.
    """
)


if "profile" not in st.session_state:

    st.warning(
        "Please create your profile first."
    )

    st.stop()


profile = st.session_state["profile"]


uploaded_image = st.file_uploader(
    "Upload an image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
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


            base64_image = (
                base64.b64encode(
                    image_bytes
                ).decode("utf-8")
            )


            client = Groq(
                api_key=st.secrets[
                    "GROQ_API_KEY"
                ]
            )


            prompt = f"""
You are EduTwin AI, a personalized visual tutor.

Student information:

Career goal:
{profile['career_goal']}

Skills:
{profile['skills']}

Education:
{profile['education']}

The student selected this explanation mode:
{mode}

Analyze the uploaded image.

First identify what is visible.

Then explain it clearly according to the selected mode.

If the image contains an educational object, diagram,
computer component, code, graph, chart, or technical concept,
explain its purpose and important concepts.

Do not invent details that cannot be observed.

Keep the explanation educational and easy to understand.
"""


            response = client.chat.completions.create(

                model="qwen/qwen3.6-27b",

                messages=[

                    {
                        "role": "user",

                        "content": [

                            {
                                "type": "text",

                                "text": prompt
                            },

                            {
                                "type": "image_url",

                                "image_url": {
                                    "url":
                                    f"data:image/jpeg;base64,{base64_image}"
                                }
                            }

                        ]
                    }

                ],

                temperature=0.4,

                max_completion_tokens=2000
            )


            answer = (
                response
                .choices[0]
                .message
                .content
            )


            st.success(
                "✅ Image analysis completed!"
            )


            st.markdown(
                answer
            )


        except Exception as error:

            st.error(
                f"Vision AI error: {error}"
            )
