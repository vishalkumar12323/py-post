from fastapi import FastAPI
from schema.schema import TodoCreateResponse, Todo, TodoGetResponse
from config.database import db

app = FastAPI(title="Todo App")

@app.post("/create-post", response_model=TodoCreateResponse)
def create_post(todo: Todo):
    db.append(todo)
    return TodoCreateResponse(todo=todo, message="Created")


@app.get("/todos", response_model=TodoGetResponse)
def fetch_todos():
    return TodoGetResponse(todos=db, message="Success")
 