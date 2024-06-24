#Driver = name, gender, age, email, license_number, phone number, vehicle [1 to 1]
from OLA_vehicle import Vehicle
class Driver:
    def __init__( self,name="NA", gender="NA", age=18, email="NA", license_number="NA", phone_number="NA", rating=2.5, vehicle= None):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email
        self.license_number = license_number
        self.phone_number = phone_number
        self.vehicle = vehicle
        self.rating = rating

    def add_driver_details(self):
        print("ENTER DRIVER DETAILS")
        self.name = input("Enter Name:")
        self.gender = input("Enter Gender:")
        self.age = input("Enter Age:")
        self.email = input("Enter Email:")
        self.license_number = input("Enter License Number:")
        self.phone_number = input("Enter Phone Number:")
        self.rating = input("Give Ratings: ")
        # 1 to 1 Mapping
        self.vehicle = Vehicle() #Object Construction
        self.vehicle.add_vehicle_details()
    def show(self):
        print("------------DRIVER------------")
        print("Name: {} | Gender: {} | Age: {}".format(self.name, self.gender, self.age))
        print("Email: {} | License Number: {}".format(self.email, self.license_number))
        print("Phone Number: {} | Ratings {}".format(self.phone_number,self.rating))
        print("-------------------------------")
        self.vehicle.show()