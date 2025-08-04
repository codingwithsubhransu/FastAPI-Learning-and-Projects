from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'Hello World'}

@app.get('/about')
def about():
    return {'message': 'CampusX is a youtube channel which teaches AIML'}