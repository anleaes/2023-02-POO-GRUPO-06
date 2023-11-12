class Order:
    def __init__(self, total_price, status, client):
        self.total_price = total_price
        self.status = status
        self.client = client
        self.order_items = []

    def __str__(self):
        return f"\nPreco Total: {self.total_price}, Status: {self.status}, Cliente: {self.client}"