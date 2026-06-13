from resume_parser import extract_text
from gemini_parser import parse_resume_with_gemini
from career_matcher import calculate_match

text = extract_text(
    r"C:\Users\sanja\OneDrive\Desktop\Sanjana_Dwivedi_DataAnalyst_deloitte.pdf"
)

resume_data = parse_resume_with_gemini(text)

skills = (
    resume_data["core_skills"]
    + resume_data["frameworks_libraries"]
    + resume_data["tools_platforms"]
)
print("CORE SKILLS")
print(resume_data["core_skills"])

print("\nFRAMEWORKS")
print(resume_data["frameworks_libraries"])

print("\nTOOLS")
print(resume_data["tools_platforms"])

print("\nALL SKILLS")
print(skills)

result = calculate_match(
    skills,
    "Data Analyst"
)

print(result)
