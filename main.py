from app.interfaces.user_interface import user_menu
from app.interfaces.product_interface import add_sample_products, show_products
from app.services.cart_service import add_to_cart
from app.services.order_service import make_order
from app.utils.file_db import load_db
from app.models.product import Product


def main():
    add_sample_products()

    user = user_menu()
    if not user:
        return

    show_products()

    product_id = int(input("\nMahsulot ID: "))
    quantity = int(input("Soni: "))

    db = load_db()
    product_data = next(p for p in db["products"] if p["id"] == product_id)

    product = Product(
        product_data["id"],
        product_data["name"],
        product_data["price"],
        product_data["stock"]
    )

    add_to_cart(user, product, quantity)

    order = make_order(user)

    print("\nBuyurtma qabul qilindi")
    print("Jami bo'lib :", order.total_price)


if __name__ == "__main__":
    main()
