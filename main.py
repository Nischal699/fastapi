from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI() #instance of FastAPI

#Decorators to define routes matters the most 
@app.get("/blog")  # Decorator to define the route or path using the HTTP GET method operation
def index(limit = 10,published : bool = True , sort: Optional[str] = None): # Path operation function
    # only get 10 blogs that are published
    if published:
       return {'data': f'{limit} publised blog from the database'}  # Return a dictionary as JSON response
    else:
        return {'data': f'{limit} all blogs from the database'}  # Return a different dictionary for all blogs

@app.get('/blog/unpublished')  # Route to get unpublished blogs
def unpublished():
    return {'data': 'unpublished blogs'}  # Return a dictionary for unpublished blogs

@app.get("/blog/{id}")  # To make path parameters dynamic {id} is a path parameter
def show(id : int):
    #fetch a blog with the given id = id 
    return {'data': id }  # Another route returning a different dictionary

@app.get("/blog/{id}/comments")  # Nested route to get comments for a specific blog
def comments(id , limit=10):
    # Fetch comments for the blog with the given id = id
    return {'data': f'comments for blog {id}'}  # Return comments for the blog with the given id


class Blog(BaseModel):
    title: str  # Blog title
    body: str   # Blog content
    published: Optional[bool] = None  # Optional field to indicate if the blog is published

@app.post("/blog")  # Route to create a new blog
def create_blog(request: Blog):  # Expecting a dictionary as the request body
    # Logic to create a new blog
    return {'data': f'Blog is created with title as {request.title}'}  # Return a confirmation message

#if __name__ == "__main__":
#    uvicorn.run(app,host="127.0.0.1", port=9000)