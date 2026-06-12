import re

def extract_email(text):

    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    return emails[0] if emails else None


def extract_phone(text):

    phones = re.findall(
        r'\b\d{10}\b',
        text
    )

    return phones[0] if phones else None


def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2 and len(line) < 40:
            return line

    return "Name Not Found"