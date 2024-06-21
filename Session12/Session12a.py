"""
    OOPS Case Study {Food Delievery App}
    Customer
    Order
    Dish

    1 customer can place many Orders
    1 Order can have many Dishes
"""
class Dish:
    def __init__(self, name="",price=0,rating=1.5):
        self.name = name
        self.price = price
        self.rating = rating
    def show(self):
        print("----------DISH------------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("---------------------------")