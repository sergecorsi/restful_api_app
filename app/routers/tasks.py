from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database, models
from app.utils import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_task(db=db, task=task, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    tasks = crud.get_tasks(db, user_id=current_user.id, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    task = crud.get_task(db, task_id=task_id, user_id=current_user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_task = crud.get_task(db, task_id=task_id, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db=db, task=task, task_id=task_id)

@router.delete("/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_task = crud.get_task(db, task_id=task_id, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.delete_task(db=db, task_id=task_id)
