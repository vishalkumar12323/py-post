from pydantic import BaseModel, ConfigDict
from typing import Optional

class Post(BaseModel):
    title: str
    description: Optional[str] = ""

    model_config = ConfigDict(extra="ignore")


class PostResponse(BaseModel):
    post: Post
    message: str