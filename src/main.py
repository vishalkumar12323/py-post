from fastapi import FastAPI
from routes.todo_routes import todo_router
from routes.user_routes import user_router


app = FastAPI(title="Todo App")


routers = [todo_router, user_router]

for router in routers:
    app.include_router(router=router, prefix="/api")