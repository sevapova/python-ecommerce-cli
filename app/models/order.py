class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.total_price = 0

    def calculate_total(self):
        self.total_price = 0
        for item in self.items:
            self.total_price += item.product.price * item.quantity
