class Restaurant:

    def __init__(self, Location, category, timings, ratings, phnno):
        print("self:", self)
        self.Location = Location
        self.category = category
        self.timings = timings
        self.ratings = ratings
        self.phnno = phnno
    
res1 = Restaurant("Ludhiana", "Veg", "10:00 A.M. - 10:00 P.M,", 4.8 , "9876544789")
print("Restaurant :", res1)
print("Restaurant data:")
print(vars(res1))

print("--------------------------------------------------------------------------")

class Menu:

    def __init__(self, category, name, numberofdishes):
        print("self:", self)
        self.category = category
        self.name = name
        self.numberofdishes = numberofdishes
    
menu1 = Menu("Italian", "pizza", 20)
print("Menu :", menu1)
print("Menu:")
print(vars(menu1))

print("--------------------------------------------------------------------------")

class Dish:

    def __init__(self, pizza, pasta, burger, noodles, bullets):
        print("self:", self)
        self.pizza = pizza
        self.pasta = pasta
        self.burger = burger
        self.noodles = noodles
        self.bullets = bullets

    
dish1 = Dish(300, 200, 60, 150, 100)
print("Dish :", dish1)
print("Dishes:")
print(vars(dish1))

print("--------------------------------------------------------------------------")