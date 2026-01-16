from fastapi import FastAPI
from data import Product
from database import getData,add_data,update_data,delete_data
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(CORSMiddleware,allow_origins=["https://localhost:3000"],allow_methods=["*"],allow_headers=["*"],)

# listOfProducts=[Product(id=1,name="laptop",description="dell laptop",price=150345,quantity=10),Product(id=2,name="laptop",description="hp laptop",price=150345,quantity=240),Product(id=3,name="laptop",description="asus laptop",price=150345,quantity=10),Product(id=4,name="laptop",description="lenevo laptop",price=150345,quantity=240)]


@app.get('/products')
def get_Products():
    return getData()

# @app.get('/products/{id}')
# def get_Product(id:int):
#     products=getData()
#     for i in listOfProducts:
#         if i.id==id:
#             return i
#     return "404 not found"

@app.post('/products/')
def add_Product(product:Product):
    return add_data(product)


@app.put("/products/{id}")
def update_product(id:int,product:Product):
    return update_data(id,product)


@app.delete('/products/{id}')
def delete_product(id:int):
    return delete_data(id)