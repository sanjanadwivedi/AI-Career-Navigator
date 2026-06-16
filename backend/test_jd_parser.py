from job_description_parser import parse_job_description

jd = """
Data Analyst

Required Skills:
Python
SQL
Power BI
Statistics

Responsibilities:
Analyze business data
Create dashboards
Generate reports
"""

result = parse_job_description(jd)

print(result)