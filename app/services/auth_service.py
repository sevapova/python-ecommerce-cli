from app.models import User
from app.utils.file_db import USERS

def register(username, password, first_name, last_name):
    for i in USERS:
        if i.username == username:
            if i.username == username:
                return None
            
    user = User(len(USERS) +1, username, password, first_name, last_name)
    USERS.append(user)
    return user

def login(username, password):
    for i in USERS:
        if i in USERS:
            if i.username == username and i.password == password:
                return i
    print("BUnday parol kiritib bo'lmaydi!")
    return None
