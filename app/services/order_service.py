from app.models.order import Order
from app.utils.file_db import ORDERS


def make_order(user):
    order = Order(user, user.cart)
    order.calculate_total()
    ORDERS.append(order)
    user.cart = []
    return order
