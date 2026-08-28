from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Legal Metrology Compliance API is running"
    }