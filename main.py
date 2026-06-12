from fastapi import FastAPI

app  = FastAPI()


#  home route
@app.get("/")
def greet():
    return "This is my landing page"



