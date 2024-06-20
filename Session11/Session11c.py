from OLA_Case_Study.OLA_Customer import Customer
print("-------------------------------------")
print("Welcome to Customer Management System")
print("-------------------------------------")


while True: 

    print("1. Add Customer")
    print("2.View Customer")
    print("0. Quit")

    choice = int(input("Enter Your Choice: "))
    print("You Selected: ", choice)

    if choice == 1:
        file = open("customer.csv", "a")
        customer = Customer()
        customer.add_customer_details()
        customer.show()

        data = customer.to_csv()
        file.write(data)
        print("Data Written")

    elif choice == 2:
        file = open("customer.csv", "r")
        lines = file.readlines()
        for line in lines:
            print(line)

    elif choice == 0:
        print("-------------------------------------")
        print("Thank You for using Customer Management System")
        print("-------------------------------------")
        file.close()
        break
