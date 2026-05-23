from fastapi import FastAPI
from pydantic import BaseModel

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


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # TODO: replace with real OpenAI/Anthropic call once provider layer is built
    return ChatResponse(
        response=f"Hello! You said: '{req.message}'. OpenAI integration coming soon.",
        model="stub-v0",
    )
