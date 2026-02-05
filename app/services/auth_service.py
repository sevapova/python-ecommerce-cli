from app.models.user import User
from app.utils.file_db import load_db, save_db


def register(username, password, first_name, last_name):
    db = load_db()

    for user in db["users"]:
        if user["username"] == username:
            print("Bunday username mavjud")
            return None

    new_user = {
        "id": len(db["users"]) + 1,
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }

    db["users"].append(new_user)
    save_db(db)

    return User(**new_user)


def login(username, password):
    db = load_db()

    for user in db["users"]:
        if user["username"] == username and user["password"] == password:
            return User(**user)

    print("Login yoki parol xato")
    return None
