class socialnetwork:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
            return f"\nRede Social: {self.name}, Descrição: {self.description}\n"