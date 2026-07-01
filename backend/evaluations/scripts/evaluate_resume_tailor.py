import json
import os
import time
import requests

API_URL = "http://127.0.0.1:8000/tailor-resume"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESUME_DIR = os.path.join(BASE_DIR, "..", "datasets", "resumes")
JD_DIR = os.path.join(BASE_DIR, "..", "datasets", "job_descriptions")
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")

os.makedirs(RESULTS_DIR, exist_ok=True)

RESULTS_FILE = os.path.join(
    RESULTS_DIR,
    "resume_tailor_results.json"
)

pdf_files = sorted(
    f for f in os.listdir(RESUME_DIR)
    if f.lower().endswith(".pdf")
)

jd_files = sorted(
    f for f in os.listdir(JD_DIR)
    if f.lower().endswith(".txt")
)

results = []

print("=" * 60)
print("Resume Tailor Evaluation")
print("=" * 60)

for resume in pdf_files:

    resume_path = os.path.join(RESUME_DIR, resume)

    for jd in jd_files:

        jd_path = os.path.join(JD_DIR, jd)

        with open(jd_path, "r", encoding="utf-8") as f:
            job_description = f.read()

        print(f"\nResume : {resume}")
        print(f"Job    : {jd}")

        start = time.time()

        try:

            with open(resume_path, "rb") as pdf:

                response = requests.post(
                    API_URL,
                    files={
                        "file": (
                            resume,
                            pdf,
                            "application/pdf",
                        )
                    },
                    data={
                        "job_description": job_description
                    },
                    timeout=180,
                )

            elapsed = round(time.time() - start, 2)

            print("Status :", response.status_code)

            if response.status_code != 200:

                print(response.text)

                results.append({
                    "resume": resume,
                    "job_description": jd,
                    "status": "FAILED",
                    "error": response.text,
                })

                continue

            output = response.json()

            results.append({
                "resume": resume,
                "job_description": jd,
                "response_time": elapsed,
                "tailored_summary": bool(
                    output.get("tailored_summary")
                ),
                "optimized_bullets": len(
                    output.get("optimized_bullets", [])
                ),
                "keywords_added": len(
                    output.get("keywords_added", [])
                ),
                "skills_to_highlight": len(
                    output.get("skills_to_highlight", [])
                ),
                "missing_keywords": len(
                    output.get("missing_keywords", [])
                ),
                "ats_improvements": len(
                    output.get("ats_improvements", [])
                ),
                "status": "PASS",
            })

            print("PASS")

        except Exception as e:

            print(e)

            results.append({
                "resume": resume,
                "job_description": jd,
                "status": "FAILED",
                "error": str(e),
            })

with open(RESULTS_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\nEvaluation Completed")
print(f"Saved to {RESULTS_FILE}")