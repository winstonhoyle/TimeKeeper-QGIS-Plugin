from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/task', response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_job_id(db, job_id=task.job_id)
    if db_task:
        raise HTTPException(status_code=400, detail='Job id already registered')
    new_task = crud.create_task(db=db, task=task)
    return new_task


@app.get('/task/all', response_model=List[schemas.Task])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@app.get('/task/{job_id}', response_model=schemas.Task)
def get_task(job_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_job_id(db, job_id=job_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return db_task


@app.delete('/task/{job_id}')
def delete_task(job_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_job_id(db, job_id=job_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    db.delete(db_task)
    db.commit()
    return {'ok': True}


@app.patch('/task/{job_id}', response_model=schemas.Task)
def update_task(job_id: int, update_data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_job_id(db, job_id=job_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail='Task not found')

    updated_task = crud.update_task(db=db, task=db_task, updated_data=update_data)
    return updated_task
