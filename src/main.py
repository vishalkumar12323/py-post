from fastapi import FastAPI
from fastapi.responses import JSONResponse
# from time import perf_counter
from routes.todo_routes import todo_router
from routes.user_routes import user_router
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware



limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Todo App")


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, lambda request, exe: JSONResponse(status_code=429, content={"detail": "To Many Request"}))

app.add_middleware(SlowAPIMiddleware)

# app.state.req_counter = 0

# @app.middleware("http")
# async def middleware(req: Request, next):
#     print(f"PATH:: {req["path"]}")
#     print(f"METHOD:: {req["method"]}")

#     payload = await req.body()
#     if payload:
#         print(payload)
    
#     start = perf_counter()
#     app.state.req_counter += 1
#     request = await next(req)

#     end = perf_counter()

#     print(f"API TIME:: {start - end}")
#     return request

routers = [todo_router, user_router]

for router in routers:
    app.include_router(router=router, prefix="/api")