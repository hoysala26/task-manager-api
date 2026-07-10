from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title : str
    description: Optional[str] = None
    completed: bool = False

class TaskResponse(Task):
    id: int