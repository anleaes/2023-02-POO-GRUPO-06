class Product:
    def __init__(self, name, description, date_fabrication, is_active, category):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        self.category = category

    def __str__(self):
        return f"\nNome: {self.name}, Descricao: {self.description}, Data de fabricaçāo:{self.date_fabrication} Ativo:{self.is_active}"