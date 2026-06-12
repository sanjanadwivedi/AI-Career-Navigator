def extract_projects(text):

    projects = []

    lines = text.split("\n")

    project_keywords = [
        "project",
        "system",
        "application",
        "dashboard",
        "chatbot",
        "prediction"
    ]

    for line in lines:

        line = line.strip()

        for keyword in project_keywords:

            if keyword.lower() in line.lower():

                if len(line) > 5:
                    projects.append(line)

    return list(set(projects))