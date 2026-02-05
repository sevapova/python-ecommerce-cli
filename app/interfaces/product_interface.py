from app.models.product import Product
from app.utils.file_db import load_db, save_db


def add_sample_products():
    db = load_db()

    if db["products"]:  
        return

    db["products"].append({
        "id": 1,
        "name": "Laptop",
        "price": 1200,
        "stock": 5
    })
    db["products"].append({
        "id": 2,
        "name": "Mouse",
        "price": 20,
        "stock": 50
    })

    save_db(db)


def show_products():
    db = load_db()

    print("\n--- Mahsulotlar ---")
    for p in db["products"]:
        print(f"{p['id']}. {p['name']} - {p['price']}$")
