class User:
    def __init__(self, id, username, password, fist_name, last_name):
        self.id = id
        self.username = username
        self.password = password
        self.fist_name = fist_name
        self.last_name = last_name
        self.cart = []
        