from fastapi import FastAPI

from app.schemas import ChatRequest
from app.agent import ask_agent

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Agent Running"}


@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_agent(request.question)

    return {
        "question": request.question,
        "answer": answer
    }