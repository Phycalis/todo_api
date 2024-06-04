from sqlalchemy import select

from api.schemas.Todo import Todo as todo_schema
from core.database import Session
from models.models import Todo


def create_todo(todo: todo_schema):
    new_todo = Todo(title=todo.title, description=todo.description)
    with Session() as session:
        session.add(new_todo)
        session.commit()


def read_todo(todo_id: int):
    with Session() as session:
        todo_query = session.execute(select(Todo).filter_by(id=todo_id)).scalar_one()
    return todo_query


def update_todo(todo: todo_schema):
    with Session() as session:
        todo_query = session.execute(select(Todo).filter_by(id=todo.id)).scalar_one()
        todo_query.title = todo.title
        todo_query.description = todo.description
        todo_query.completed = todo.completed
        session.commit()


def delete_todo(todo_id: int):
    with Session() as session:
        todo_query = session.execute(select(Todo).filter_by(id=todo_id)).scalar_one()
        session.delete(todo_query)
        session.commit()

