from resume_parser import extract_text
from gemini_parser import parse_resume_with_gemini

text = extract_text(r"C:\Users\sanja\OneDrive\Desktop\Sanjana_Dwivedi_DataAnalyst_deloitte.pdf")

result = parse_resume_with_gemini(text)

print(result)