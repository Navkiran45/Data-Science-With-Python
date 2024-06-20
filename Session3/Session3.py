#OPERATORS
#ARITHMETIC OPERATORS
# +,-,*,**,/,//, %

product_price = 200
gst_tax = 0.18

price_to_pay = product_price + gst_tax*product_price
print(price_to_pay, type(price_to_pay), id(price_to_pay))

number = 10
result = number/3 #will give decimal values
result = number // 3 #will give integral number
print("result is: ", result)

base = 2
result = base * 2
result = base ** 3 #this means raise to power
print("result now is: ", result)

#Remainder Operator: %
bucket_size = 7
hashcode = 120% bucket_size
print("Hashcode of 120 is: ",hashcode)

#ASSIGNMENT OPERATOR
# =, =+, -=, *=, **=, /=, //=, %=

#A new reference variable age will be created in Stack
# A container 20 will be created in Heap
# Hashcode of 20 will be stored in age
# Hence, age is REFERENCE VARIABLE
age = 20

#UPDATE OPERATOR 
age = age + 10
age +=10 #Shorthand operator add and assign
print("age is: ", age)

age %= 3
age -= 1

print("Age now is: ", age)

#INCREMENT AND DECREMENT
qty = 1
qty += 1 #2 
qty -= 1 # 1
qty += 5 # 6
qty -= 1 # 5
qty **= 2 # 5 power 2 -> 25
print("Quantity is: ",  qty)
