from fastapi import FastAPI
from schema.schema import Post, PostResponse

app = FastAPI(title="Todo API", description="This API only for development purpose", version="0.1.1")

@app.get("/", summary="Index", description="Index route for checking API health.")
def index():
    return {"msg": "API running...."}


@app.post("/create-post", response_model=PostResponse, summary="Create new post")
def create_post(post: Post) -> PostResponse:
    return PostResponse(post=post, message="Created")


@app.put("/update-post/{post_id}", summary="Update Exisiting post")
def update_post(post_id: str, post: Post):
    return {
        "update_post": post,
        "post_id": post_id,
        "is_edited": True
    }