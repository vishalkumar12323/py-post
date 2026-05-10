from fastapi import HTTPException, APIRouter, Response, Request
from schema.schema import BaseResponse, Todo, TodoCreateResponse, TodoGetResponse, TodoUpdateResponse, UpdateTodoBody, UUID
from config.database import db
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
todo_router = APIRouter(prefix="/todo", tags=["Todos APIs"])


# Route for create new todo with unique id
@todo_router.post("/create-post", response_model=TodoCreateResponse, name="Create New Post")
@limiter.limit("2/minute")
def create_post(request: Request, todo: Todo):
    db.append(todo)
    return Response(content=TodoCreateResponse(todo=todo, message="Created").model_dump_json(), status_code=201)

# Route for fetch all todos
@todo_router.get("/todos", response_model=TodoGetResponse)
def fetch_todos():
    return Response(content=TodoGetResponse(todos=db, message="Success").model_dump_json(), status_code=200)


# Route for fetch todo by its id
@todo_router.get("/todo/{todo_id}", response_model=Todo)
def fetch_todo_by_id(todo_id: str):
    try:
        todo_id = UUID(todo_id)
    except Exception as ex:
        return Response(content=BaseResponse(message="Wrong UUID", err=str(ex)).model_dump_json(), status_code=400)
        
    print(todo_id)
    for todo in db:
        if str(todo.id) == str(todo_id):
            return Response(content=todo, status_code=200)
    return Response(content=BaseResponse(message="Not found").model_dump_json(), status_code=404)
    

# Helper function for find todo using id in list database
def find_todo(todo_id: str):
    for i in range(len(db)):
        if str(db[i].id) == todo_id:
            print(db[i])
            return i
    return -1

# Route for delete existing todo from the db
@todo_router.delete("/todo/{todo_id}")
def delete_todo_by_id(todo_id:str):
    todo_idx = find_todo(todo_id=todo_id)
    if todo_idx != -1:
        db.pop(todo_idx)
        return Response(content={"message": "Todo deleted"}, status_code=200)
    raise HTTPException(status_code=404, detail="Todo not found")


# Route for update todo using todo id
@todo_router.put("/update-todo/{todo_id}", response_model=TodoUpdateResponse | BaseResponse)
def update_todo(todo_id: str, data: UpdateTodoBody):
    try:
        todo_id = UUID(todo_id)
    except Exception as err:
        return Response(content=BaseResponse(message="Wrong UUID", err=str(err)).model_dump_json(), status_code=400)
    
    todo_idx = find_todo(todo_id=str(todo_id))

    if todo_idx == -1:
        return Response(content=BaseResponse(message="Todo not found").model_dump_json(), status_code=404)
    todo = db[todo_idx]
    todo.name = data.name
    todo.category = data.category
    todo.completed = data.completed

    return Response(content=TodoUpdateResponse(todo=todo).model_dump_json(), status_code=200)


# Route for fetch all categorial todos
@todo_router.get("/todos/search", response_model=TodoGetResponse|BaseResponse, name="Fetch todos by category")
def fetch_by_category(category: str):
    todos = [todo for todo in db if todo.category == category]

    if not todos:
        return Response(content=TodoGetResponse(todos=[], message="No any todos").model_dump_json(), status_code=404)
    
    return Response(content=TodoGetResponse(todos=todos).model_dump_json(), status_code=200)

    