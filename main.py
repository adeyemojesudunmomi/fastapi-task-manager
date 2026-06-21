from fastapi import FastAPI

app = FastAPI(title="Task Manager API")

@app.get("/")
def home():
    return {"message": "Task Manager API Running"}