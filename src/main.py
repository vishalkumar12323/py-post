from fastapi import FastAPI, HTTPException
from schema.schema import TodoCreateResponse, Todo, TodoGetResponse, BaseResponse, UpdateTodoBody, TodoUpdateResponse
from config.database import db
from uuid import UUID


app = FastAPI(title="Todo App")

# Route for create new todo with unique id
@app.post("/create-post", response_model=TodoCreateResponse)
def create_post(todo: Todo):
    db.append(todo)
    return TodoCreateResponse(todo=todo, message="Created")

# Route for fetch all todos
@app.get("/todos", response_model=TodoGetResponse)
def fetch_todos():
    return TodoGetResponse(todos=db, message="Success")


# Route for fetch todo by its id
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
    

# Helper function for find todo using id in list database
def find_todo(todo_id: str):
    for i in range(len(db)):
        if str(db[i].id) == todo_id:
            print(db[i])
            return i
    return -1

# Route for delete existing todo from the db
@app.delete("/todo/{todo_id}")
def delete_todo_by_id(todo_id:str):
    todo_idx = find_todo(todo_id=todo_id)
    print(todo_idx)
    if todo_idx != -1:
        db.pop(todo_idx)
        return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")


# Route for update todo using todo id
@app.put("/update-todo/{todo_id}", response_model=TodoUpdateResponse | BaseResponse)
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


# Route for fetch all categorial todos
@app.get("/todos/search", response_model=TodoGetResponse|BaseResponse)
def fetch_by_category(category: str) -> TodoGetResponse|BaseResponse:
    todos = [todo for todo in db if todo.category == category]

    if not todos:
        return TodoGetResponse(todos=[], message="No any todos")
    
    return TodoGetResponse(todos=todos)


