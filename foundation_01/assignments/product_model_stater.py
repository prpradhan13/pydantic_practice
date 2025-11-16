from pydantic import BaseModel

# TODO: Create Product model with id, name, price, in_stock

class ProductModel(BaseModel):
    id: int
    name: str
    price: float
    in_stock: int

prod_01 = {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "in_stock": 25
}

product = ProductModel(**prod_01)
print(product)