from datetime import datetime

from sqlalchemy.orm import Session

from . import models, schemas


def get_task_by_job_id(db: Session, job_id: int):
    return db.query(models.Task).filter(models.Task.job_id == job_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        name=task.name, job_id=task.job_id, status=task.status, file_name=task.file_name
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task: schemas.Task, updated_data: schemas.TaskCreate):
    for var, value in vars(updated_data).items():
        setattr(task, var, value) if value else None

    if updated_data.status == models.Status.WORKING and not task.started:
        task.started = task.last_modified

    if updated_data.status == models.Status.COMPLETED:
        task.completed = task.last_modified
        if task.started:
            task.time_elapsed = task.completed - task.started

    db.commit()
    db.refresh(task)
    return task
