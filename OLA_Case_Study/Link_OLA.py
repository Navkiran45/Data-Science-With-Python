from OLA_Case_Study.OLA_Customer import Customer
from OLA_Case_Study.OLA_driver import Driver
from OLA_Case_Study.OLA_vehicle import Vehicle
from OLA_Case_Study.OLA_ride import Ride

#Driver Application
driver = Driver()
driver.add_driver_details()

#Customer Application
customer = Customer()
customer.add_customer_details()

#Server
ride = Ride()
ride.add_ride_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("Ride Booked")