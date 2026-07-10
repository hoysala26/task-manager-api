from fastapi import FastAPI, HTTPException
from models import Task, TaskResponse

app = FastAPI()

tasks = []
next_id = 1
@app.get("/")
def root():
    return {"message": "Task Manager API is running"}
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks
@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    global next_id
    new_task = task.dict()
    new_task["id"] = next_id
    tasks.append(new_task)
    next_id += 1
    return new_task
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task.dict())
            return task
    raise HTTPException(status_code=404, detail="Task not found")
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")
