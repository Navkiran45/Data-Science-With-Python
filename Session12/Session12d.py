from Session12a import Dish
from Session12b import Order
from Session12c import Customer

dishes_menu = [Dish(name="Dal Makhani", price= 700, rating=4.5),Dish(name="Paneer Makhani", 
price=650,rating=4.0), Dish(name="Noodles", price=300, rating=3.5), Dish(name="Pizza",
price=450,rating=3.8), Dish(name="Burger", price=200,rating=4.3)]

customer1 = Customer(name="John", phone= "+91 99999 22222", email="john@example.com", address="Model Town")
customer2 = Customer(name="Jack", phone= "+91 99999 44444", email="jack@example.com", address="New Model Town")

#Hard Coding: We as developer are linking objects
"""
order1 = Order(oid=1, dishes= [dishes_menu[0], dishes_menu[3]], customer= customer1, total=1150)
order2 = Order(oid=1, dishes= [dishes_menu[1], dishes_menu[2], dishes_menu[4]], customer= customer1, total=1250)
"""

order1 = Order(oid=1)
order1.link_customer(customer1)
order1.link_dishes(dishes =  [dishes_menu[0], dishes_menu[3]])
order1.show()

order2 = Order(oid=2)
order2.link_customer(customer1)
order2.link_dishes(dishes = [dishes_menu[1], dishes_menu[2], dishes_menu[4]])
order2.show()