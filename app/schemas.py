from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .models import Status


class TaskBase(BaseModel):
    pass


class TaskCreate(TaskBase):
    name: str
    job_id: int
    status: Status
    file_name: str


class Task(TaskBase):
    id: int
    name: str
    job_id: int
    status: Status
    file_name: str
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True


class TaskUpdate(TaskBase):
    name: Optional[str] = None
    status: Optional[Status] = Status.WORKING
    file_name: Optional[str] = None
