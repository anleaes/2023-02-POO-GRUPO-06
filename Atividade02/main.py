from category import Category
from client import Client
from clientsocialnetwork import Clientsocialnetwork
from order import Order
from orderItem import OrderItem
from product import Product
from socialnetwork import Socialnetwork

def main ():
    client1 = Client("Maria", "Silva", "Rua X 2122", "323648", "MariaSilvia@gmail.com", "Feminno"  )
    client2 = Client("Jean", "Paul", "Baile dos Coroados 2000", '51 991323575', "McJeanPaul@hotmail.com", "Masculino" )
    client3 = Client("Nicole", "Kidman", "Oxford Lane 23", "215550112", "Nkidman@yahoo.com", "Feminino" )

    category1 = Category("1", "Eletroportateis", "Linha branca domestica")
    category2 = Category ("2", 'Destilados', "Whiskey, Tequila, Gin, Vodka, Cachaca")
    category3 = Category("3", "Cutelaria", "Facas, Garfos") 

    product1 = Product("Geladeira French Door ", "01-02-2023","True ")
    product2 = Product("Jean Bean" "02-02-2008", "True")
    product2 = Product ("Cutelo Tramontina", "10-11-2023", "False")

if __name__ == "__main__":
        main()
        