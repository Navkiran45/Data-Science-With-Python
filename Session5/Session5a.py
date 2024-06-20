#Main function
# Need not to make main function while coding in python
# But if you want to transfer any other lang progam which is having main fn, u have to go this procedure to have main fn in python

def main():
    print("Hello All")
    a = 10
    b = 20
    c = a + b
    print("Sum of ",a, "and", b, "is:", c)

#print("__name__ is:", __name__)
# __name__ will have value as __main__ 
# __name__ is a magic variable (dunder) will have value as __main__

if __name__ == "__main__":
    main()
