from fastapi import FastAPI, HTTPException
from schema.schema import TodoCreateResponse, Todo, TodoGetResponse, BaseResponse, UpdateTodoBody, TodoUpdateResponse
from config.database import db
from uuid import UUID


app = FastAPI(title="Todo App")

@app.post("/create-post", response_model=TodoCreateResponse)
def create_post(todo: Todo):
    db.append(todo)
    return TodoCreateResponse(todo=todo, message="Created")


@app.get("/todos", response_model=TodoGetResponse)
def fetch_todos():
    return TodoGetResponse(todos=db, message="Success")


@app.get("/todo/{todo_id}", response_model=Todo | BaseResponse)
def fetch_todo_by_id(todo_id: str) -> Todo | BaseResponse:
    try:
        todo_id = UUID(todo_id)
    except Exception as ex:
        return BaseResponse(message="Wrong UUID", err=str(ex))
        
    print(todo_id)
    for todo in db:
        if str(todo.id) == str(todo_id):
            return todo
    return BaseResponse(message="Not found")
    
        
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


@app.put("/update-name/{todo_id}", response_model=TodoUpdateResponse | BaseResponse)
def update_todo(todo_id: str, data: UpdateTodoBody) -> TodoUpdateResponse | BaseResponse:
    try:
        todo_id = UUID(todo_id)
    except Exception as err:
        return BaseResponse(message="Wrong UUID", err=str(err))
    
    todo_idx = find_todo(todo_id=str(todo_id))

    if todo_idx == -1:
        return BaseResponse(message="Todo not found")
    todo = db[todo_idx]
    todo.name = data.name
    todo.category = data.category
    todo.completed = data.completed

    return TodoUpdateResponse(todo=todo)


