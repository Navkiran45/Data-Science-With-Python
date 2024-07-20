from Session17a import Patient
from Session17b import Consultation
from Session17d import Database
from tabulate import tabulate

def main():
    print("~~~~~~~~~~~DOCTOR'S APP~~~~~~~~~~~~~~")
    print("~~~~~~Welcome to Doctor's App~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    mydb = Database()

    while True:
        print("1. Add New Patient")
        print("2. Update Existing Paient")
        print("3. Delete Existing Patient")
        print("4. View Patient by Phone")
        print("5. View Patient by PID")
        print("6. View All Patients")
        print("7. Add Consultation for Patient")
        print("8. View All Consultations")
        print("9. View Consultation for a Patient")
        print("10. View Followups")
        print("0. To Quit App")

        choice = int(input("Enter Your Choice:"))

        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "Insert into Doc_Patient values (null, '{name}', '{phone}', '{dob}', '{email}', '{gender}', '{created_on}')".format_map(vars(patient))

            mydb.write(sql)
            print("[Doc's APP]" , patient.name, "Saved in Database")
     
        elif choice == 2:
            pid = int(input("Enter Patient's ID to Update:"))
            sql = "select * from Doc_Patient where pid= '{}'".format(pid)
            rows = mydb.read(sql)
            print(rows)
            
            patient = Patient(pid=rows[0][0], name=rows[0][1], phone=rows[0][2], dob=rows[0][3], email=rows[0][4], gender=rows[0][5])
            print("Patient to Update:")
            patient.show()
            patient.update_patient_details()

            sql = "Update Doc_Patient set name = '{name}', phone = '{phone}', DOB={dob}, email ='{email}', gender= '{gender}', created_on = '{created_on}' where pid = {pid}".format_map(vars(patient))
            mydb.write(sql)
            patient.show()
        
        elif choice == 3:
            pid = int(input("Enter the Patient ID to be deleted: "))
            sql = "delete from Doc_Patient where pid = {}".format(pid)

            ask = input("Are you sure you want to delete (yes/no): ")
            if ask == "yes":
                mydb.write(sql)
                print("[Patient]", pid , "deleted from Database")
            else:
                print("Delete Operation Skipped")

        elif choice == 4:
            phone = input("Enter Patient's Phone Number: ")
            sql = "Select * from Doc_Patient where phone = '{}'".format(phone)
            rows = mydb.read(sql)
            columns = ["Patient ID", "Name", "Phone Number", "DOB", "Email ID", "Gender", "Created On"]
            print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 5:
            pid = int(input("Enter Patient ID: "))
            sql = "Select * from Doc_Patient where pid = '{}'".format(pid)
            rows = mydb.read(sql)
            columns = ["Patient ID", "Name", "Phone Number", "DOB", "Email ID", "Gender", "Created On"]
            print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 6:
            sql = "Select * from Doc_Patient"
            rows = mydb.read(sql)
            columns = ["Patient ID", "Name", "Phone Number", "DOB", "Email ID", "Gender", "Created On"]
            print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 7:
             consultation = Consultation()
             consultation.add_consultation_details()
             sql = "Insert into Consultation values(null, {pid}, '{remarks}', '{medicines}', '{next_followup}', '{created_on}')".format_map(vars(consultation))
             mydb.write(sql)
             print("Consultation Added..")

        elif choice == 8:
             sql = "Select * from Consultation"
             rows = mydb.read(sql)
             columns = ["Patient ID", "Consultation ID", "Remarks", "Medicines", "Next Followup", "Created On"]
             print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 9:
             pid = input("Enter Patient ID: ")
             sql = "Select * from Consultation where pid = {}".format(pid)
             rows = mydb.read(sql)
             columns = ["Patient ID", "Consultation ID", "Remarks", "Medicines", "Next Followup", "Created On"]
             print(tabulate(rows, headers= columns, tablefmt = 'grid'))
        
        elif choice == 10:
             start_date = input("Enter Start Date (yyyy-mm-dd hh:mm:ss): ")
             end_date = input("Enter End Date (yyyy-mm-dd hh:mm:ss): ")
             sql = "Select * from Consultation where next_followup >= '{}' and next_followup <= '{}'".format(start_date, end_date)
             rows = mydb.read(sql)
             columns = ["Patient ID", "Consultation ID", "Remarks", "Medicines", "Next Followup", "Created On"]
             print(tabulate(rows, headers= columns, tablefmt = 'grid'))
        
        elif choice == 0:
             print("Thankyou for using Doctor's App!")
             break
        
        else:
            print("Inavlid Choice")

if __name__ == "__main__":
        main()