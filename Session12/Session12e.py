# Dish: Name, Price, Rating

class Dish:
    def __init__(self, name="",price=0,rating=1.5):
        self.name = name
        self.price = price
        self.rating = rating
    def show(self):
        print("----------DISH------------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("---------------------------")

def bubble_sort(data):
    for i in range(0,len(data)-1):

        for j in range(0, len(data)-i-1):
            if data[j].price > data[j+1].price:
                #Swap Operation
                data[j], data[j+1] = data[j+1], data[j]
        print()

dishes = [Dish(name="Dal Makhani", price= 700, rating=4.5),Dish(name="Paneer Makhani", 
price=650,rating=4.0), Dish(name="Noodles", price=300, rating=3.5), Dish(name="Pizza",
price=450,rating=3.8), Dish(name="Burger", price=200,rating=4.3)]


print("Dishes")
for dish in dishes:
    dish.show()

bubble_sort(dishes)

print("Sorted Dishes")
for dish in dishes:
    dish.show()