from career_matcher import calculate_match

skills = [
    "Python",
    "SQL",
    "Power BI",
    "Excel"
]

result = calculate_match(
    skills,
    "Data Analyst"
)

print(result)