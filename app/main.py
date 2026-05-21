from fastapi import FastAPI

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
