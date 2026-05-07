from fastapi import FastAPI, Request
from time import perf_counter
from routes.todo_routes import todo_router
from routes.user_routes import user_router



app = FastAPI(title="Todo App")

@app.middleware("http")
async def middleware(req: Request, next):
    print(f"PATH:: {req["path"]}")
    print(f"METHOD:: {req["method"]}")

    payload = await req.body()
    if payload:
        print(payload)
    
    start = perf_counter()
    request = await next(req)

    end = perf_counter()

    print(f"API TIME:: {start - end}")
    return request

routers = [todo_router, user_router]

for router in routers:
    app.include_router(router=router, prefix="/api")