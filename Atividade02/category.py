class Category:
    def __init__(self, id, name , description ):
        self.id = id
        self.name = name
        self.description = description
        

    def __str__(self):
            return f"\n Categoria {self.name},  Descricao: {self.description}"