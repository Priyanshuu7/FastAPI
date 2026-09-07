from fastapi import FastAPI

app  = FastAPI()


#  home route
@app.get("/")
def greet():
    return "This is my landing page"


@app.get("/about")
def about_page():
    return "This my fastapi project about page"

