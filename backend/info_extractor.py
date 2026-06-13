import re


def extract_email(text):

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""


def extract_phone(text):

    pattern = r'(\+91[- ]?)?[6-9]\d{9}'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:15]:

        line = line.strip()

        if (
            len(line) > 3
            and len(line.split()) <= 4
            and "@" not in line
            and not any(char.isdigit() for char in line)
        ):
            return line.upper()

    return ""