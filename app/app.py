from fastapi import FastAPI, HTTPException


app = FastAPI()

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "Hello World"}
text_post = {1: {"title": "New Post", "Content": "Cool test post"}}

@app.post("/posts")

def get_all_posts():
    return text_post

@app.get("/posts/{id}")

def get_post(id: int):
    return text_post.get(id)