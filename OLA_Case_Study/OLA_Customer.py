#Customer = name, phn_no, email, address, gender, age
class Customer:
    def __init__(self, name="NA", phn_no="NA", email="NA", address="NA", gender="NA", age=15):
        self.name = name
        self.phn_no = phn_no
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age
    def add_customer_details(self):
        print("ENTER CUSTOMER DETAILS")
        self.name = input("Enter Name: ")
        self.phn_no = input("Enter Phone Number: ")
        self.email = input("Enter Email: ")
        self.address = input("Enter Address: ")
        self.gender = input("Enter Gender: ")
        self.age = int(input("Enter Age: "))
    def show(self):
        print("------------CUSTOMER------------")
        print("Name: {} | Phone Number: {}".format(self.name, self.phn_no))
        print("Email: {} | Address: {}".format(self.email, self.address))
        print("Gender: {} | Age: {}".format(self.gender, self.age))
        print("--------------------------------")

    def to_csv(self):
        data = "{},{},{},{},{}\n".format(self.name, self.phn_no, self.email, self.address, self.gender, self.age)
        return data
    