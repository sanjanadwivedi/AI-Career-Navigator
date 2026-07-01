import json
import os
import time
import requests

API_URL = "http://127.0.0.1:8000/analyze-job-fit"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RESUME_DIR = os.path.join(BASE_DIR, "..", "datasets", "resumes")
JD_DIR = os.path.join(BASE_DIR, "..", "datasets", "job_descriptions")
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")

os.makedirs(RESULTS_DIR, exist_ok=True)

RESULTS_FILE = os.path.join(RESULTS_DIR, "job_match_results.json")

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
print("Job Match Evaluation")
print("=" * 60)

for resume in pdf_files:

    resume_path = os.path.join(RESUME_DIR, resume)

    for jd in jd_files:

        print(f"\nResume : {resume}")
        print(f"Job    : {jd}")

        jd_path = os.path.join(JD_DIR, jd)

        with open(jd_path, "r", encoding="utf-8") as f:
            job_description = f.read()

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

            job_match = output.get("job_match", {})

            results.append({
                "resume": resume,
                "job_description": jd,
                "response_time": elapsed,
                "match_score": job_match.get("match_score"),
                "matched_skills": len(job_match.get("matched_skills", [])),
                "missing_skills": len(job_match.get("missing_skills", [])),
                "resume_improvements": len(output.get("resume_improvements", [])),
                "interview_questions": len(output.get("interview_questions", [])),
                "roadmap_steps": len(output.get("roadmap", [])),
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