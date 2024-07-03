from Session16a import Patient
from Session16b import Database
from tabulate import tabulate

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Patient Management App")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    mydb = Database()

    while True:
        print("1. Add New Patient")
        print("2. Update Existing Paient")
        print("3. Delete Existing Patient")
        print("4. View Patient by Phone")
        print("5. View Patient by PID")
        print("6. View All Patients")
        print("0. To Quit App")

        choice = int(input("Enter Your Choice:"))

        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "Insert into Patient values (null, '{name}', '{phone}', {age}, '{email}', '{gender}', '{created_on}')".format_map(vars(patient))

            mydb.write(sql)
            print("[PMS APP]" , patient.name, "Saved in Database")
        
        elif choice == 2:
            pid = int(input("Enter Patient's ID to Update:"))
            sql = "select * from Customer where cid= '{}'".format(pid)
            rows = mydb.read(sql)
            print(rows)
            
            patient = Patient(pid=rows[0][0], name=rows[0][1], phone=rows[0][2], age=rows[0][3], email=rows[0][4], gender=rows[0][5])
            print("Patient to Update:")
            patient.show()
            patient.update_patient_details()

            sql = "Update Patient set name = '{name}', phone = '{phone}', email ='{email}', age={age}, gender= '{gender}', created_on = '{created_on}' where pid = {pd}".format_map(vars(patient))
            mydb.write(sql)
            patient.show()

        elif choice == 3:
            pid = int(input("Enter the Patient ID to be deleted: "))
            sql = "Delete from Patient where pid = {}".format(pid)

            ask = input("Are you sure you want to delete (yes/no): ")
            if ask == "yes":
                mydb.write(sql)
                print("[PMS APP]", pid , "deleted from Database")
            else:
                print("Delete Operation Skipped")

        elif choice == 4:
            phone = input("Enter Patient's Phone Number: ")
            sql = "Select * from Patient where phone = '{}'".format(phone)
            rows = mydb.read(sql)
            columns = ["Patient ID", "Name", "Phone Number", "Age", "Email ID", "Gender", "Created On"]
            print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 5:
            pid = int(input("Enter Patient ID: "))
            sql = "Select * from Patient where pid = '{}'".format(pid)
            rows = mydb.read(sql)
            columns = ["Patient ID", "Name", "Phone Number", "Age", "Email ID", "Gender", "Created On"]
            print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 6:
            sql = "Select * from Patient"
            rows = mydb.read(sql)
            columns = ["Patient ID", "Name", "Phone Number", "Age", "Email ID", "Gender", "Created On"]
            print(tabulate(rows, headers= columns, tablefmt = 'grid'))

        elif choice == 0:
            print("Thankyou for using [PMS APP]")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
