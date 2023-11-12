from category import Category
from client import Client
from clientsocialnetwork import Clientsocialnetwork
from order import Order
from orderItem import OrderItem
from product import Product
from socialnetwork import Socialnetwork

def main():
    client1 = Client("Maria", "Silva", "Rua X 2122", "323648", "MariaSilvia@gmail.com", "Feminino")
    client2 = Client("Jean", "Paul", "Baile dos Coroados 2000", '51 991323575', "McJeanPaul@hotmail.com", "Masculino")
    client3 = Client("Nicole", "Kidman", "Oxford Lane 23", "215550112", "Nkidman@yahoo.com", "Feminino")

    category1 = Category(1, "Eletroportateis", "Linha branca domestica")
    category2 = Category(2, "Destilados", "Whiskey, Tequila, Gin, Vodka, Cachaca")
    category3 = Category(3, "Cutelaria", "Facas, Garfos")
    category4 = Category(4, "Roupas", "Camisas, Calças, Moletons")

    product1 = Product("Geladeira French Door", "Eletrodoméstico para cozinha", "01-02-2023", True, category1)
    product2 = Product("Whisky Jack Daniel's", "Autêntico Tennessee Whiskey", "22-06-2023", True, category2)
    product3 = Product("Cutelo Tramontina", "Faca para churrasco", "10-11-2023", False, category3)
    product4 = Product("Jean Bean", "Calça jeans de alta qualidade", "18-04-2020", True, category4)

    print("Clientes:")
    print(client1)
    print(client2)
    print(client3)

    print("\nCategorias:")
    print(category1)
    print(category2)
    print(category3)
    print(category4)

    print("\nProdutos:")
    print(product1)
    print(product2)
    print(product3)
    print(product4)

if __name__ == "__main__":
    main()
