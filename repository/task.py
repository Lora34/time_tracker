from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from database.database import get_db_session
from models import Tasks, Categories 
from schema.task import Task



class TaskRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_tasks(self):
        with self.db_session() as session:
            task = session.execute(select(Tasks)).scalars().all()
        return task
    
    def get_task(self, task_id: int) -> Tasks | None:
        query = select(Tasks).where(Tasks.id == task_id)
        with self.db_session() as session:
            task = session.execute(query).scalar()
        return task
    def create_task(self, task: Task) -> int:
        #task = Tasks(id=5,name="text name",pomodoro_count=4,category_id=1)
        task_model = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id)
        with self.db_session() as session:
            session.add(task_model)
            session.commit()
    def delete_task(self, task_id: int) -> None:
        query = delete(Tasks).where(Tasks.id == task_id)
        with self.db_session() as session:
            session.execute(query)  
            session.commit()   
    def get_task_by_category_name(self, category_name: str) -> list[Tasks]:
        query = select(Tasks).join(Categories, Tasks.category_id == Categories.id).where(Categories.name == category_name)
        with self.db_session() as session:
            session.execute(query).scalar().all()  
            session.commit()   
    def update_task_name(self, task_id: int, name: str) -> Tasks:
        query = update(Tasks).where(Tasks.id==task_id).values(name=name).returning(Task.id)
        with self.db_session() as session:
            task_id: int = session.execute(query).scalar_one_to_one()
            return self.get_task(task_id)

