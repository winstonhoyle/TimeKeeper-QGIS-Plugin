from typing import Optional
from datetime import datetime, timedelta

from pydantic import BaseModel

from .models import Status


class TaskBase(BaseModel):
    pass


class TaskCreate(TaskBase):
    name: str
    job_id: int
    status: Status
    file_name: Optional[str] = None


class Task(TaskBase):
    id: int
    name: str
    job_id: int
    status: Status
    file_name: str = None
    created: datetime
    last_modified: datetime
    started: datetime = None
    completed: datetime = None
    time_elapsed: timedelta = None

    class Config:
        orm_mode = True


class TaskUpdate(TaskBase):
    name: Optional[str] = None
    status: Optional[Status] = Status.WORKING
    file_name: Optional[str] = None
