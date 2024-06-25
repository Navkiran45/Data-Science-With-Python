class employee:
    def __init__(self, name="NA", age=18, field ="NA", position= "", salary= 0):
        self.name = name
        self.age = age
        self.field = field
        self.position = position
        self.salary = salary

    def add_details(self):
        self.name = input("Enter Employee's Name:")
        self.age = int(input("Enter Employee's Age:"))
        self.field = input("Enter Employee's Field:")
        self.position = input("Enter Employee's Position:")
        self.salary = input("Enter Employee's Salary:")
        
    def show(self):
        print("~~~~~~~~~~~EMPLOYEE~~~~~~~~~~~")
        print("{} | {} | {} ".format(self.name, self.age, self.field))
        print("{} | {} ".format(self.position, self.salary))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")