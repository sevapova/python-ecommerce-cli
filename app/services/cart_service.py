from app.models.cart import CartItem


def add_to_cart(user, product, quantity):
    user.cart.append(CartItem(product, quantity))


def remove_from_cart(user, product_id):
    user.cart = [
        item for item in user.cart
        if item.product.id != product_id
    ]
