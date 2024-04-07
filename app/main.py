# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Status": "not dead yet!"}

@app.get("/review")
async def review_resume():
    # TODO: integrate with Langchain for resume review

    return {"message": "Resume review endpoint."}
