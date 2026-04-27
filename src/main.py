from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "something"}


@app.post("/create-post")
def create_post(post: dict):
    return {
        "Post": post,
        "msg": "Created"
    }