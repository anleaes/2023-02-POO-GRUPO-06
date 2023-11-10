class Client:
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender

    def __str__(self):
            return f"\nPrimeiro Nome: {self.first_name}, Ultimo Nome: {self.last_name}, Endereço: {self.address}, Celular: {self.cell_phone}, Email: {self.email}, Genero: {self.gender}"