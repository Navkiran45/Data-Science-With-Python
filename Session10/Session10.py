# NO FUNCTION OVERLOADING
def add(num1,num2):
    result = num1 + num2
    print("Result is: {}".format(result))

print("Add is: ", add) # add is a function and you will see hashcode of function

#Execute the add function
add(10,20)

#Reference Copy operation
hello = add
hello(11,22)

#If you redefine the same function, previous fn will be removed from memory and new defination will exist
def add(num1, num2, num3):
    result = num1 + num2 +num3 + 10
    print("Result is: ",result)

add(10,20,30)
