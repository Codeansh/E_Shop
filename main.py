from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status, Depends
from fastapi.params import Body
from db import cursor, conn
from  models import Product
app = FastAPI()

# TEST ROUTE
@app.get("/")
def root():
    return {"message": "Succesful testing"}

# GET ALL PRODUCTS LIST

@app.get("/products")
def view_products():
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    return {"Products": products}


# GET A PRODUCT BY ID
@app.get("/products/{id}")
def get_product(id: int):
    cursor.execute('''SELECT * FROM products WHERE id = %s''',(str(id),))
    product = cursor.fetchone()
    if product  is None:
        raise HTTPException(404, " product was not found ")
    return {"Found product": product}


# ADD A PRODUCT
@app.post("/products",status_code=201)
def add_product(product: Product):
    cursor.execute('''INSERT INTO products (name,price) VALUES ( %s, %b ) RETURNING *''',(product.name,product.price))
    conn.commit()
    return {"Product added": product}


# UPDATE A PRODUCT
@app.put("/products/{id}")
def update_product(id: int, product: Product):
    cursor.execute('''UPDATE products SET name = %s ,price = %s WHERE id = %s RETURNING *''',(product.name,product.price,str(id)))
    product = cursor.fetchone()
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" product was not found ")
    conn.commit()
    return {"Product updated": product}

# DELETE A PRODUCT
@app.delete("/products/{id}")
def delete_product(id:int,response:Response):
    cursor.execute('''DELETE FROM products WHERE id = %s RETURNING *''', (str(id),))
    product = cursor.fetchone()
    if product is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message" : "Product was not found"}
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
