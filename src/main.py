from fastapi import FastAPI, HTTPException
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


@app.get("/todo/{todo_id}", response_model=Todo)
def fetch_todo_by_id(todo_id: str):
    for todo in db:
        if str(todo.id) == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
    
        
def find_todo(todo_id: str):
    for i in range(len(db)):
        if str(db[i].id) == todo_id:
            print(db[i])
            return i
    return -1

@app.delete("/todo/{todo_id}")
def delete_todo_by_id(todo_id:str):
    todo_idx = find_todo(todo_id=todo_id)
    print(todo_idx)
    if todo_idx != -1:
        db.pop(todo_idx)
        return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")