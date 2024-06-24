# OLA/ Uber Case Study
"""
Driver has a vehicle
Customer can book Ride(s)
"""

"""
Driver = name, gender, age, email, license_number, phone number, vehicle [1 to 1]
1 driver has 1 vehicle
Vehicle = reg_number, brand, color, model 
Customer = name, phn_no, email, address, gender, age
Ride = customer[1 to 1], date,time,from_location, to_location, distance fare,driver[1 to 1]
1 ride has 1 customer
1 ride has 1 driver
"""

class Vehicle:
    def __init__(self, reg_number="NA", brand="NA", color="white", model="NA"):
        self.reg_number = reg_number
        self.brand = brand
        self.color = color
        self.model = model

    def add_vehicle_details(self):
        print("ENTER VEHICLE DETAILS")
        self.reg_number = input("Enter Registration number: ")
        self.brand = input("Enter brand: ")
        self.color = input("Enter color: ")
        self.model = input("Enter model: ")

    def show(self):
        print("------------VEHICLE--------------")
        print("Number: {} | Brand: {}".format(self.reg_number, self.brand))
        print("Model: {} | Color: {}".format(self.model, self.color))
        print("---------------------------------")
"""
vehicle = Vehicle(reg_number="PB10HI8055", brand="Hundai", model="i20",color="white")
vehicle = Vehicle()
vehicle.add_vehicle_details()
vehicle.show()
"""
