#from Session9 import Dish
class Menu:
    def __init__(self, name="NA", number_of_dishes=0,menu_dishes=[]):
        self.name = name
        self.number_of_dishes = number_of_dishes
        self.menu_dishes = menu_dishes
    
    def show(self):
        print("------------------------------")
        print("Menu: {} | {}".format(self.name, self.number_of_dishes))
        print("------------------------------")

        print("Dishes:")
        for idx in range(len(self.menu_dishes)):
            self.menu_dishes[idx].show()
"""
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

menu.show()
"""