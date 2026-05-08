from fastapi import APIRouter, Request
from datetime import datetime
from slowapi import Limiter
from slowapi.util import get_remote_address

user_router = APIRouter(prefix="/user", tags=["User APIs"])


limiter = Limiter(key_func=get_remote_address)


@user_router.post("/signup")
@limiter.limit("2/minute")
def signup(req: Request):
    return {
        "status": "success",
        "user_count" : req.app.state.req_counter
    }


@user_router.post("/signin")
def signin():
    return {
        "status": "success",
        "user_id": str(datetime.second)
    }

@user_router.get("/users")
def get_users():
    return [
        {"user_id": str(datetime.second)}, {"user_id": str(datetime.second)}, {"user_id": str(datetime.second)}
    ]