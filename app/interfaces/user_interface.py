from app.services.auth_service import register, login

def user_interface():
    print("\n1. Register")
    print("2. Login")

    choice = input("Menyuni tanlang: ")

    if choice == "1":
        return register(
            input("Username:"),
            input("Password:"),
            input("First Name:"), 
            input("Last Name:")
        )
    
    elif choice == "2":
        return login(
            input("Username:"),
            input("Password:")
        )
    
    else:
        print("Bunday menyu yo'q!")
        return None