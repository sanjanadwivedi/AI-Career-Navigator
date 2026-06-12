SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Tableau",
    "Flutter",
    "FastAPI",
    "Machine Learning",
    "Deep Learning",
    "Java",
    "C++"
]

def extract_skills(text):

    found = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found.append(skill)

    return found