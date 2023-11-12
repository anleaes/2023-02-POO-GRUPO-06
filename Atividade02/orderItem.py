class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product
        order.order_items.append(self)

    def __str__(self):
        return f"\nQuantidade: {self.quantity}, Preco Unitario: {self.unitary_price}, Ordem: {self.order}, Produto: {self.product}"