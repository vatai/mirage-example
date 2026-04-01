#!/usr/bin/env python3
import base64
import io

from openai import OpenAI
from PIL import Image

from get_api_key import get_api_key


def main():
    # Generate a blank image.

    img = Image.new("RGB", (224, 224), color=(255, 255, 255))
    img.save("/tmp/emptyimg.png")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    img_bytes = buf.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    # Send it to ChatGPT

    # If you get an error, you can simply replace the `get_api_key()`
    # function call with the string which holds your API key.
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-5.1",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{img_base64}",
                    },  # fake image
                    {
                        "type": "input_text",
                        "text": "What abnormality is present in this chest X-ray?",
                    },
                ],
            }
        ],
    )

    # Print the response

    print(response.output_text)


if __name__ == "__main__":
    main()
