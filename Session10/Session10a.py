def add(num1, num2, num3):
    result = num1 + num2 + num3
    print("Result is: {}".format(result))

add(10,20,30)
add(num1=10, num3=30, num2=20)

#Default arguments/inputs
def square(num=5):
    result = num*num
    print("Result is: {}".format(result))

square()
square(3)
square(num=9)

#def subract(num1=10, num2): #error
def subtract(num1, num2=5): #if num1 is given default value num2 will show error 
    # but if num2 is given default value num1 will not show error
    # give values to right side variables 
    result = num1- num2
    print("Result is: {}".format(result))

subtract(num1=10)
