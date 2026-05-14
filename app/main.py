from fastapi import FastAPI
from pydantic import BaseModel
from .tasks import long_task
from .celery_app import celery_app

app = FastAPI(title="Atlas Distributed Orchestrator", version="1.0")

class TaskRequest(BaseModel):
    seconds: int = 10

@app.get("/")
async def root():
    return {
        "message": "🚀 Atlas Distributed Orchestrator is live!",
        "docs": "/docs",
        "flower_monitor": "http://localhost:5555"
    }

@app.post("/tasks/")
async def create_task(request: TaskRequest):
    task = long_task.delay(request.seconds)
    return {
        "task_id": task.id,
        "status": "queued",
        "message": "Task sent to queue successfully"
    }

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None,
        "progress": result.info if isinstance(result.info, dict) else None
    }