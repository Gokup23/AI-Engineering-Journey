from fastapi import FastAPI                 #import

app = FastAPI()              # instance 
@app.get('/')          #decorator to provide path for the function
def index():           #function
    return {'data' : {'name' : 'Gopal'}}

@app.get('/about')       # a subpage with its own url 
def about():
    return {'data': {'about page'}}