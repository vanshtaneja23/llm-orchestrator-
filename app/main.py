import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(
    title="LLM Orchestrator",
    description="Multi-provider LLM routing with caching and observability",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"name": "LLM Orchestrator", "version": "0.1.0"}


@app.get("/health")
def health():
    return {"status": "ok"}


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: int


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": req.message}],
            max_tokens=100,
        )
    except Exception as exc:
        logger.error("OpenAI API call failed: %s", exc)
        raise HTTPException(status_code=503, detail=f"OpenAI API call failed: {exc}")

    return ChatResponse(
        response=completion.choices[0].message.content,
        model="gpt-4o-mini",
        tokens_used=completion.usage.total_tokens,
    )
