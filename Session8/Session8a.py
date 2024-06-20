"""
    Principle of OOPS:
    1. Think of an Object

    FlightBooking: fromLocation, toLocation, travelDate, numberOfTravllers, travelClass
"""

# 2. Create class of object
# Below class represents the object. It is description of objectclass FlightBooking:
class FlightBooking:

    #Default Constructor in Python
    # self is reference variable, which will hold the hashcode of current object
    def __init__(self):
        print("self: ",self)
        self.fromLocation = "New delhi"
        self.toLocation = "bengaluru"
        self.travelDate = "18 June 2023"
        self.numberOfTravellers = 1
        self.tavelClass = "Economy"

     # Parameterized Constructor
    def __init__(self, fromLocation, toLocation, travelDate, numberOfTravllers, travelClass):
        print("self:", self)
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.travelDate = travelDate
        self.numberOfTravllers = numberOfTravllers
        self.travelClass = travelClass

booking1 = FlightBooking()
print("Booking1: ", booking1)
print("Booking1 data:")
print(vars(booking1))

booking2 = FlightBooking()
print("Booking2: ", booking1)
print("Booking2 data:")
print(vars(booking2))