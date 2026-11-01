from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My First CI/CD Project"}

@app.get("/health")
def health():
    return {"status": "healthy"}