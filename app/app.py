from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "Hello World"}
text_posts = {
    1: {"title": "New Post", "Content": "Cool test post"},
    2: {"title": "Hello World", "Content": "This is a simple hello world post for testing."},
    3: {"title": "Flutter Update", "Content": "Testing state management and UI rebuild behavior."},
    4: {"title": "Backend Notes", "Content": "FastAPI integration with a mock data source."},
    5: {"title": "Daily Log", "Content": "Basic dummy content to validate list rendering."},
    6: {"title": "Performance Test", "Content": "Checking how the app handles multiple posts."},
    7: {"title": "Draft Post", "Content": "This content is not finalized and used for testing only."},
    8: {"title": "Release Notes", "Content": "Minor bug fixes and performance improvements."},
    9: {"title": "Sraft Post", "Content": "This content is not finalized and used for testing only."},
    10: {"title": "Helease Notes", "Content": "Minor bug fixes and performance improvements."}
}


@app.get("/posts")

def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")

def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post Not Found" )
    return text_posts.get(id)

@app.post("/posts")

def create_post(post: PostCreate) -> PostResponse:
    new_post = {'title': post.title,"Content": post.content }
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post

