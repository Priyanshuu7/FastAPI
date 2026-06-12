from fastapi import FastAPI

app  = FastAPI()


#  home route
#  
@app.get("/")
def greet():
    return "Hello, World!"

Products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "quantity": 10, "description": "A high-performance laptop."},
    {"id": 2, "name": "Smartphone", "price": 499.99, "quantity": 20, "description": "A powerful smartphone with a great camera."},
    {"id": 3, "name": "Headphones", "price": 199, "quantity": 30, "description": "A pair of headphones for listening to music."},
]


@app.get("/products")
def get_products():
    return Products