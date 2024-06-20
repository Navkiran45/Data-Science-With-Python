"""
    Code 3 Objects
    1. Dish : name, price, rating
    2. Menu : name, number_of_dishes, dishes 
        1 Menu can have many Dishes (1 to many)
    3. Restaurant : name, phone, email, address, operating_hours, ratings, menu
        1 Restaurant can have 1 Meny (1 to 1)

"""

class Dish:
    def __init__(self, name="NA", price=0, rating= 1.5):
        self.name = name #copy the contents of name(input) to the self.name
        self.price = price
        self.rating = rating

    def show(self):
        print("--------------------------------------------")
        print("Dish {} | {} | {}".format(self.name, self.price, self.rating))
        print("--------------------------------------------")

"""dish1 = Dish()
#print("dish1: ", hex(id(dish1)))

dish2 = Dish("Dal Makhani", 250, 4.5)
#print("dish2: ", hex(id(dish2)))

dish3 = Dish("Paneer Masala", 350, 4.8)
#print("dish3: ", hex(id(dish3)))

#List of dishes
dishes = [dish1, dish2, dish3]
print("DISHES: ")
for idx in range(len(dishes)):
    dishes[idx].show()"""

dishes = [
    Dish(), 
    Dish("Dal Makhani", 250, 4.5), 
    Dish("Paneer Masala", 350, 4.8)
    ]
print("DISHES: ")
for idx in range(len(dishes)):
    dishes[idx].show()