import json
import os
import time
import requests

API_URL = "http://127.0.0.1:8000/upload-resume"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESUME_DIR = os.path.join(BASE_DIR, "..", "datasets", "resumes")
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")
RESULTS_FILE = os.path.join(RESULTS_DIR, "resume_results.json")

os.makedirs(RESULTS_DIR, exist_ok=True)

print("=" * 60)
print("Resume Evaluation Started")
print("=" * 60)
print("Resume Directory:", RESUME_DIR)
print("API:", API_URL)
print()

pdf_files = sorted(
    f for f in os.listdir(RESUME_DIR)
    if f.lower().endswith(".pdf")
)

print(f"Found {len(pdf_files)} PDF(s)\n")

results = []

for index, filename in enumerate(pdf_files, start=1):

    print("=" * 60)
    print(f"[{index}/{len(pdf_files)}] {filename}")

    pdf_path = os.path.join(RESUME_DIR, filename)

    try:

        start = time.time()

        with open(pdf_path, "rb") as pdf:

            response = requests.post(
                API_URL,
                files={
                    "file": (
                        filename,
                        pdf,
                        "application/pdf",
                    )
                },
                timeout=180,
            )

        elapsed = round(time.time() - start, 2)

        print(f"Response Time : {elapsed}s")
        print(f"Status Code   : {response.status_code}")

        if response.status_code != 200:

            print("❌ API Error")

            results.append({
                "resume": filename,
                "status": "FAILED",
                "status_code": response.status_code,
                "response_time": elapsed,
                "error": response.text,
            })

            continue

        data = response.json()

        resume = data.get("resume_analysis", {})

        skills = (
            resume.get("core_skills", [])
            + resume.get("frameworks_libraries", [])
            + resume.get("tools_platforms", [])
        )

        result = {
            "resume": filename,
            "status": "PASS",
            "response_time": elapsed,
            "ats_score": resume.get("ats_score"),
            "recommended_roles": resume.get("recommended_roles", []),
            "experience_level": resume.get("experience_level"),
            "skills_count": len(skills),
            "projects_count": len(resume.get("projects", [])),
            "experience_count": len(resume.get("experience", [])),
            "education_present": bool(resume.get("education")),
            "strengths_count": len(resume.get("strengths", [])),
            "weaknesses_count": len(resume.get("weaknesses", [])),
            "missing_skills_count": len(resume.get("missing_skills", [])),
        }

        results.append(result)

        print("✅ Resume parsed successfully")

    except Exception as e:

        print(f"❌ Error: {e}")

        results.append({
            "resume": filename,
            "status": "FAILED",
            "error": str(e),
        })

print("\nSaving results...")

with open(RESULTS_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\n" + "=" * 60)
print("Resume Evaluation Completed")
print(f"Results saved to:\n{RESULTS_FILE}")
print("=" * 60)