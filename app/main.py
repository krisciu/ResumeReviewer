# app/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import Union
from app.utils.constants import SUPPORTED_FILE_TYPES
from app.review.resume_parser import parse_resume
from app.review.reviewer import analyze_resume

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Status": "not dead yet!"}

@app.post("/review")
async def review_resume(file: UploadFile = File(...)):
    content_type = file.content_type
    
    if content_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="File type not supported")
    resume_text = parse_resume(await file.read(), content_type)
    review = analyze_resume(resume_text)
    return {"review": review}
