from fastapi import FastAPI, UploadFile, File
import shutil

from resume_parser import extract_text
from gemini_parser import parse_resume_with_gemini

app = FastAPI()


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    resume_data = parse_resume_with_gemini(text)

    return resume_data


@app.get("/")
def home():
    return {"message": "AI Career Navigator API Running"}