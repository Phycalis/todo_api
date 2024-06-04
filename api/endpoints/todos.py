from fastapi import APIRouter

from api.crud.crud import create_todo, read_todo, update_todo, delete_todo
from api.schemas.Todo import Todo

router = APIRouter(prefix="/todos",
                   tags=["Todos"])


@router.get("")
def get_todos(todo_id: int):
    todo = read_todo(todo_id)
    return {"status": 200, "message": todo}


@router.post("")
def new_todo(todo: Todo):
    create_todo(todo)
    return {"status": 201, "message": f'Todo created = {todo.model_dump()}'}


@router.post("/update")
def upd_todo(todo: Todo):
    update_todo(todo)
    return {"status": 200, "message": f'Todo updated= {todo.model_dump()}'}


@router.delete("/delete")
def del_todo(todo_id: int):
    delete_todo(todo_id)
    return {"status": 200, "message": f'Todo deleted'}
