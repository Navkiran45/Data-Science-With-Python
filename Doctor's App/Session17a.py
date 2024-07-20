"""
DOCTOR'S APP
Doctor -> User of Application
Patient -> pid, name, phone, dob, email. gender
Consultation -> cid, pid, remarks, medicines, next_followup, created_on

"""
import datetime

"""
SQL Query
create table Doc_Patient( 
pid int primary key auto_increment,
name varchar(256),
phone varchar(20),
dob date,
email varchar(256),
gender varchar(20),
created_on datetime
);
"""

class Patient:
    def __init__(self, pid=0, name= "NA",phone="", dob="", email= "", gender="" ):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.dob = dob
        self.email = email
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def add_patient_details(self):
        self.name = input("Enter Patient's Name: ")
        self.phone = input("Enter Phone Number: ")
        self.dob = input("Enter Patient's DOB (yyyy-mm-dd): ")
        self.email = input("Enter Email Id: ")
        self.gender = input("Enter Patient's Gender: ")

    def update_patient_details(self):
        name = input("Enter Name: ")
        if len(name) != 0:
            self.name = name
        phone = input("Enter Phone Number: ")
        if len(phone) != 0:
            self.phone = phone
        dob = input("Enter DOB (yyyy-mm-dd): ")
        if len(dob) != 0:
            self.dob = dob
        email = input("Enter Email: ")
        if len(email) != 0:
            self.email = email
        gender = input("Enter Gender: ")
        if len(gender) != 0:
            self.gender = gender

    def show(self):
        print("------------PATIENT-----------------")
        patient = """
        {pid} |{name} | {phone}
        {email} | {dob}
        {gender} | {created_on}
        """.format_map(vars(self))
        
        print(patient)
