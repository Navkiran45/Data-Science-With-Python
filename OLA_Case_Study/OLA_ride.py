from OLA_Customer import Customer
from OLA_driver import Driver
from OLA_vehicle import Vehicle

class Ride:
    def __init__(self, customer= None, date= "20 June 2024", time ="12:00", from_location="Home", to_location="Work", distance=4, fare= 200, driver= None):
        self.customer = customer
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.distance = distance
        self.fare = fare
        self.driver = driver

    def add_ride_details(self):
        print("ENTER RIDE DETAILS")
        self.from_location = input("Enter From Location: ")
        self.to_location = input("Enter To Location: ")

    def link_customer(self, customer):
        self.customer = customer

    def link_driver(self, driver):
        self.driver = driver
        
    def show(self):
        self.customer.show()
        print("------------RIDE---------------")
        print("From: {} | To: {} ".format(self.from_location, self.to_location))
        print("Distance: {} | Fare: {}".format(self.distance, self.fare))
        print("Date: {} | Time {}".format(self.date,self.time))
        print("-------------------------------")   
        self.driver.show()
