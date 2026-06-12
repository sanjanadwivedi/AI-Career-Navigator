def extract_education(text):

    education_keywords = [
        "B.Sc",
        "Bachelor",
        "Computer Science",
        "B.Tech",
        "M.Tech",
        "M.Sc",
        "MBA"
    ]

    education = []

    lines = text.split("\n")

    for line in lines:

        for keyword in education_keywords:

            if keyword.lower() in line.lower():

                education.append(line.strip())

    return list(set(education))