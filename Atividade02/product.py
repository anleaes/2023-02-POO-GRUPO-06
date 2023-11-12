from category import Category

class Product:
    def __init__(self, name, description, date_fabrication, is_active):
        super() .__init__( id, name , description)
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        

    def __str__(self):
            return f"\n Nome: {self.name}, Descricao: {self.description}, Data de fabricaçāo:{self.date_fabrication} Ativo:{self.is_active} "