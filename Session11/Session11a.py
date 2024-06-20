name = input("Enter Name: ")
phone = input("Enter Phone: ")
email = input("Enter email: ")

customer_details = "{},{},{}\n".format(name, phone, email)

file = open("customer.csv", "a")
file.write(customer_details)
print("Customer Data Saved..")
file.close()