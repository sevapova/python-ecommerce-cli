class Order:
    def __init__(self, id, user, items):
        self.id = id
        self.user = user
        self.items = items
        self.total_price = 0

    def calculate_total(self):
        for item in self.items:
            self.total_price += item.product.price * item.quantity