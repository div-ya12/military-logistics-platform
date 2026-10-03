from fastapi import FastAPI

app = FastAPI(
    title="Military Logistics Platform",
    description="AI-powered logistics platform for remote and high-altitude Army posts.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Military Logistics Platform API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }