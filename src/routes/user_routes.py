from fastapi import APIRouter, Request
from datetime import datetime
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

user_router = APIRouter(prefix="/user", tags=["User APIs"])


@user_router.post("/signup")
@limiter.limit("2/minute")
def signup(request: Request):
    return {
        "status": "success",
        "user_count" : 2
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