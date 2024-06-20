from Session9.Session9 import Dish
from Session9.Session9a import Menu

class Restaurant:

    def __init__(self, name="NA", phone="NA", email="NA", address="NA",operating_hours="10:00 to 23:00", ratings = 2.5, menu= None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hours = operating_hours
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("RESTAURANT")
        print("------------------------------")
        print("Restaurant: {} | {} | {}".format(self.name, self.phone, self.email))
        print("Address: {} | {} | {}".format(self.address, self.operating_hours,self.ratings))
        print("------------------------------")

        self.menu.show()

dishes = [
    Dish(),
    Dish("Dal Makhani", 250, 4.5),
    Dish("Panner Masala", 350, 3.9)
]

menu = Menu(
    name = "Indian Veggie Delight",
    number_of_dishes = len(dishes),
    menu_dishes = dishes
)

Restaurant(name= "Veggie", 
           phone="+91 99898 00988", 
           email="abc@com", 
           address= "Krishna Nagar", 
           ratings= 4.5,
           menu = menu
           ).show()