from app.interfaces.user_interface import user_menu
from app.interfaces.product_interface import add_sample_products, show_products
from app.services.cart_service import add_to_cart
from app.services.order_service import make_order
from app.utils.file_db import PRODUCTS


def main():
    add_sample_products()

    user = user_menu()
    if not user:
        return

    show_products()

    product_id = int(input("\nID: "))
    quantity = int(input("Soni: "))

    product = next(p for p in PRODUCTS if p.id == product_id)
    add_to_cart(user, product, quantity)

    order = make_order(user)

    print("\nBuyurtma qabul qilindi")
    print("Jami summa:", order.total_price)


if __name__ == "__main__":
    main()
