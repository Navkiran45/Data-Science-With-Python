#OOPS: Object Oriented Programming Structure
#Object: Anything which exists in reality is a object. [It is a customised storage container. ]
#Class: Drawing of object [Class is representation/drawing of an object which we code]

#Principle of OOPS:
# 1.Think of an Object
# 2. Create its class.
# 3. Using class create Real Object

"""
Mr. John wants to get a food delievery application created.
Customer sbould be able to register. Restaurants should list menu of dishes. Customer should
be able to place an order. An order can have many dishes and restaurant will acceot/reject the order. 
Once the order is accepted delievery agent will fulfill the order.
"""

"""
Customer: name,phone,email, gender, address, etc.
Restaurant: name, phone, email, address, operaringHours, pricePerPerson, category, ratings, etc.
Menu: name, numberOfDishes, type
 
"""

"""
Object
GitRepo: commits, sharelink, branch

"""
# FlightBooking: from,to, travelDate, numberOfTravlers, travelClass

# 2. Create class of object
#Below class represents the object. It is description of object
class FlightBooking:
    pass

# 3. Create the real object from class in Memory
#Below is: Object Construction Statement
booking1 = FlightBooking()
booking2 = FlightBooking()
booking3 = FlightBooking()
#booking1 is a reference variable, FlightBooking() - represent the object constructor
print(booking1)
print(id(booking1))

booking3 = booking1

#Operations on Object
# 1. WRITE OPERATION
booking1.fromLocation = "Delhi"
booking1.toLocation = "Goa"
booking1.travelDate = "15 July, 2024"
booking1.numberOfTravellers = 3
booking1.travelClass = "Economy"

booking2.fromLocation = "Delhi"
booking2.toLocation = "Goa"
booking2.travelDate = "15 July, 2024"
booking2.numberOfTravellers = 3
booking2.travelClass = "Economy"
booking2.bookedAt = "12:30 17, June 2024"

# 2. UPDATE OPERATION
booking1.fromLocation = "Chandigarh"
booking1.numberOfTravellers = 2

# 3. READ OPERATION
print("Booking 1 data: ")
print(vars(booking1))
print("FROM: ",booking1.fromLocation , "TO: ", booking1.toLocation)

print("Booking 2 data: ")
print(vars(booking2))
print("FROM: ",booking2.fromLocation , "TO: ", booking2.toLocation)

print("Booking 3 data: ")
print(vars(booking3))
print("FROM: ",booking3.fromLocation , "TO: ", booking3.toLocation)

# 4. DELETE OPERATION
del booking1.travelClass

print("Booking 1 data after deletion: ")
print(vars(booking1))
print("FROM: ",booking1.fromLocation , "TO: ", booking1.toLocation)

print("Booking 3 data after deletion: ")
print(vars(booking3))
print("FROM: ",booking3.fromLocation , "TO: ", booking3.toLocation)
