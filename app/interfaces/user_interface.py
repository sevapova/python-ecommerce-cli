from app.services.auth_service import register, login


def user_menu():
    print("\n1. Register")
    print("2. Login")

    choice = input("Tanlang: ")

    if choice == "1":
        return register(
            input("Username: "),
            input("Password: "),
            input("First name: "),
            input("Last name: ")
        )

    elif choice == "2":
        return login(
            input("Username: "),
            input("Password: ")
        )

    else:
        print("Bunday menu yo'q!")
        return None
