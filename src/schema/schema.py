from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional

class Todo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    category: str
    status: bool


class BaseResponse(BaseModel):
    message: str
    err: Optional[str] = None


class TodoCreateResponse(BaseResponse):
    todo: Todo

class TodoGetResponse(BaseResponse):
    todos: list[Todo]