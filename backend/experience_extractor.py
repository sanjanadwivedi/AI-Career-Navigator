def extract_experience(text):

    experience = []

    experience_keywords = [
        "intern",
        "internship",
        "experience",
        "trainee",
        "worked"
    ]

    lines = text.split("\n")

    for line in lines:

        for keyword in experience_keywords:

            if keyword.lower() in line.lower():

                experience.append(line.strip())

    return list(set(experience))