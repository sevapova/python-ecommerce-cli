from app.models.order import Order
from app.utils.file_db import load_db, save_db


def make_order(user):
    db = load_db()

    order = Order(user, user.cart)
    order.calculate_total()

    db["orders"].append({
        "id": len(db["orders"]) + 1,
        "user_id": user.id,
        "total_price": order.total_price
    })

    save_db(db)
    user.cart = []

    return order
