from fastapi import FastAPI

app = FastAPI() #instance of FastAPI


@app.get("/")  # Decorator to define the route
def index():
    return {'data':{'name': 'John', 'age': 30, 'city': 'New York'}}  # Return a dictionary as JSON response

@app.get("/about")  # Another route
def about():
    return {'data':{'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}}  # Another route returning a different dictionary