
import datetime

class Patient:
    def __init__(self, pid=0, name= "NA",phone="", age="", email= "", gender="" ):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def update_patient_details(self):
        name = input("Enter Name: ")
        if len(name) != 0:
            self.name = name
        phone = input("Enter Phone Number: ")
        if len(phone) != 0:
            self.phone = phone
        age = input("Enter Age: ")
        if len(age) != 0:
            self.age = int(age)
        email = input("Enter Email: ")
        if len(email) != 0:
            self.email = email
        gender = input("Enter Gender: ")
        if len(gender) != 0:
            self.gender = gender

    def add_patient_details(self):
        self.name = input("Enter Patient's Name: ")
        self.phone = input("Enter Phone Number: ")
        self.age = int(input("Enter Patient's Age: "))
        self.email = input("Enter Email Id: ")
        self.gender = input("Enter Patient's Gender: ")

    def show(self):
        print("------------PATIENT-----------------")
        print("Patient ID: {}".format(self.pid))
        print("Name: {} | Phone Number: {}".format(self.name, self.phone))
        print("Email: {} ".format(self.email))
        print("Gender: {} | Age: {}".format(self.gender, self.age))
        print("-------------------------------------")