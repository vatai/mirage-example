import os
import re
import subprocess
import sys


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
