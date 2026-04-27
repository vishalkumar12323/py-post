from fastapi import FastAPI
from schema.schema import Post, PostResponse

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "something"}


@app.post("/create-post", response_model=PostResponse)
def create_post(post: Post):
    return {
        "post": post,
        "message": "Created"
    }