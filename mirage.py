#!/usr/bin/env python3
import base64
import io
import os
import re
import subprocess
import sys

from openai import OpenAI
from PIL import Image


def get_api_key():
    try:
        result = subprocess.run(
            [
                "gpg",
                "-q",
                "--decrypt",
                "--batch",
                "--yes",
                "--no-tty",
                f"{os.path.expanduser('~')}/.authinfo.gpg",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print("Error decrypting .authinfo.gpg:", e.stderr, file=sys.stderr)
        sys.exit(1)

    content = result.stdout

    # Extract API key from authinfo format
    match = re.search(
        r"machine\s+api\.openai\.com\s+login\s+\S+\s+password\s+(\S+)", content
    )
    if not match:
        print("Could not find API key in .authinfo.gpg", file=sys.stderr)
        sys.exit(1)

    return match.group(1)


def main():
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)
    img = Image.new("RGB", (224, 224), color=(255, 255, 255))
    img.save("/tmp/emptyimg.png")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    img_bytes = buf.getvalue()

    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

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

    print(response.output_text)


if __name__ == "__main__":
    main()
