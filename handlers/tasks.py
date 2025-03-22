
from fastapi import APIRouter, status, Depends
from typing import Annotated
from repository import TaskRepository
from database.database import get_db_connection
from fixture import tasks as fixture_tasks
from repository.cache_task import TaskCache
from schema.task import TaskSchema
from dependency import get_task_service, get_tasks_repository, get_tasks_cache_repository
from service import TaskService


router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.get(
        "/all",
        response_model=list[TaskSchema]
        )
async def get_tasks(
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)],
    task_cache: Annotated[TaskCache, Depends(get_tasks_cache_repository)],
    task_service: Annotated[TaskService, Depends(get_task_service)]
    ):
    return task_service.get_tasks()


@router.post(
        "/", 
        response_model=TaskSchema
        )
async def create_task(
        task: TaskSchema,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
    ):
    task_id = task_repository.create_task(task)
    task.id = task_id
    #connection = get_db_connection()
    #cursor = connection.cursor()
    #cursor.execute("INSERT INTO Tasks (name, pomodoro_count, category_id) VALUES (?, ?, ?)", (task.name, task.pomodoro_count, task.category_id))
    #connection.commit()
    #connection.close()
    return task

@router.patch(
        "/{task_id}", 
        response_model=TaskSchema
        )
async def patch_task(
        task_id: int, 
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
    ):
        return task_repository.update_task_name(task_id, name)

    #connection = get_db_connection()
    #cursor = connection.cursor()
    #cursor.execute("UPDATE Tasks SET name =? WHERE id=?", (name, task_id))
    #connection.commit()
    #task = cursor.execute("SELECT * FROM Tasks WHERE id=?", f"{task_id}").fetchall()[0]
    #connection.close()
    #return TaskSchema(
    #    id=task[0],
    #    name=task[1],
    #    pomodoro_count=task[2],
    #    category_id=task[3]
    #)

@router.delete(
        "/{task_id}", 
        status_code=status.HTTP_204_NO_CONTENT
        )
async def delete_task(
    task_id: int,
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
     task_repository.delete_task(task_id)
    #connection = get_db_connection()
    #cursor = connection.cursor()
    #cursor.execute("DELETE FROM Tasks WHERE id =?", (task_id,))
    #connection.commit()
    #connection.close()
    #return {"message": "task deleted"}