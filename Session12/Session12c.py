class Customer:
    def __init__(self, name="",phone=0,email=1.5, address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def show(self):
        print("----------CUSTOMER------------")
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("{}".format(self.address))
        print("---------------------------")


