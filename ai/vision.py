import base64

from groq import Groq


VISION_MODEL = "qwen/qwen3.6-27b"


def encode_image(image_bytes):

    return base64.b64encode(
        image_bytes
    ).decode("utf-8")


def analyze_image(
    api_key,
    image_bytes,
    prompt
):

    client = Groq(
        api_key=api_key
    )

    encoded_image = encode_image(
        image_bytes
    )

    response = client.chat.completions.create(
        model=VISION_MODEL,

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
                            "url": (
                                "data:image/jpeg;base64,"
                                + encoded_image
                            )
                        }
                    }
                ]
            }
        ],

        temperature=0.4,

        max_completion_tokens=700,

        reasoning_effort="none"
    )

    return (
        response
        .choices[0]
        .message
        .content
    )
