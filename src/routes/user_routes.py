from fastapi import APIRouter
from datetime import datetime

user_router = APIRouter(prefix="/user", tags=["User APIs"])

@user_router.post("/signup")
def signup():
    return {
        "status": "success",
        "user_id": str(datetime.second)
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