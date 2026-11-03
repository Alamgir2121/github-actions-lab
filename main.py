from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My First CI/CD Project"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/v1/info")
def app_info():
    return {
        "application": "GitHub Actions Lab",
        "version": "1.0.0",
        "environment": "development"
    }