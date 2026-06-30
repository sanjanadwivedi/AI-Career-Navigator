SKILL_ALIASES = {

    "Machine Learning": [
        "Machine Learning",
        "ML Modelling",
        "Scikit-learn"
    ],

    "Data Visualization": [
        "Data Visualisation",
        "Power BI",
        "Tableau",
        "Matplotlib",
        "Seaborn"
    ],

    "Statistics": [
        "Statistical Analysis",
        "Statistics"
    ],

    "LLMs": [
        "LLM",
        "Transformers",
        "Generative AI"
    ],
    "LangChain": [
    "langchain",
    "retrieval",
    "agent"
],
    "Scikit-learn": [
    "Scikit-learn",
    "Sklearn"
],
"Deep Learning": [
    "Neural Networks",
    "Deep Learning"
],
"Data Annotation & Labeling": [
    "annotation",
    "labeling",
    "annotated",
    "labelled",
    "dataset annotation"
],

"Data Quality Control": [
    "quality control",
    "quality assurance",
    "validation",
    "data validation",
    "evaluation"
],

"Data Preprocessing": [
    "data preprocessing",
    "preprocessing",
    "data cleaning",
    "cleaning",
    "normalisation",
    "normalization",
    "pipeline",
    "data pipeline"
],

"Attention to Detail": [
    "accuracy",
    "attention to detail",
    "quality",
    "consistency",
    "error detection"
]
}

ROLE_DATABASE = {

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics",
        "Tableau"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "Deep Learning",
        "Data Visualization"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "LLMs",
        "LangChain",
        "RAG",
        "Vector Databases"
    ],

    "Business Analyst": [
        "Excel",
        "SQL",
        "Power BI",
        "Business Analysis",
        "Requirements Gathering"
    ],
    "Data Annotation Specialist": [
    "Python",
    "SQL",
    "Data Annotation & Labeling",
    "Data Quality Control",
    "Data Preprocessing",
    "Attention to Detail"],
    
    "Machine Learning Engineer": [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Statistics",
    "SQL",
    "Scikit-learn"]
}


def calculate_match(user_skills, target_role):

    required_skills = ROLE_DATABASE.get(target_role, [])

    matched_skills = []
    missing_skills = []

    user_skills_lower = [
        skill.lower()
        for skill in user_skills
    ]

    for skill in required_skills:
        aliases = SKILL_ALIASES.get(skill, [skill])
        found = any(
        alias.lower() in user_skill.lower()
        for alias in aliases
        for user_skill in user_skills)
        
        if found:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    match_score = round(
        (len(matched_skills) / len(required_skills)) * 100
    ) if required_skills else 0

    return {
        "target_role": target_role,
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
def calculate_all_role_matches(user_skills):

    results = []

    for role in ROLE_DATABASE:

        result = calculate_match(
            user_skills,
            role
        )

        results.append({
    "role": role,
    "score": result["match_score"],
    "matched_skills": result["matched_skills"],
    "missing_skills": result["missing_skills"]
})

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results