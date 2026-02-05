from app.models.product import Product
from app.models.cart import CartItem
from app.utils.file_db import PRODUCTS

def add_product():
    PRODUCTS.append(Product(1, "TV", 1000, 10))
    PRODUCTS.append(Product(2, "Laptop", 1500, 5))
    PRODUCTS.append(Product(3, "Phone", 500, 20))


def show_products():
    print("\n------ Mahsulotlar -----")
    for i in PRODUCTS:
        print(f"{i.id}. {i.name} - ${i.price} (Stock: {i.stock})")