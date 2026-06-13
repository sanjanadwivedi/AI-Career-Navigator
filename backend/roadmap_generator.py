ROADMAP_DATABASE = {
    "Statistics": {
        "resources": [
            "Khan Academy Statistics",
            "StatQuest YouTube"
        ],
        "project": "Analyze sales data using descriptive statistics"
    },

    "Tableau": {
        "resources": [
            "Tableau Public Tutorials",
            "DataCamp Tableau Course"
        ],
        "project": "Build an interactive sales dashboard"
    },

    "AWS": {
        "resources": [
            "AWS Cloud Practitioner",
            "AWS Skill Builder"
        ],
        "project": "Deploy a data dashboard on AWS"
    }
}


def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        if skill in ROADMAP_DATABASE:

            roadmap.append({
                "skill": skill,
                "resources": ROADMAP_DATABASE[skill]["resources"],
                "project": ROADMAP_DATABASE[skill]["project"]
            })

    return roadmap