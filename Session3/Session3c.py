# BItwise Operators
# &, |, ^

num1 = 10
num2 = 8 

print("num1 in binary is: ", bin(num1))
print("num2 in binary is: ", bin(num2))

result1 = num1 & num2 # AND 1 0 0 0 -> 8
result2 = num1 | num2 # OR 1 0 1 0 -> 10
result3 = num1 ^ num2 # XOR 0 0 1 0 -> 2
print("Result1: ", result1)
print("Result2: ", result2)
print("Result3: ", result3)

#Shift Operators 
#IMPORTANT
# >>, << 
num1 = 8
num2 = 3

# dividing by 2 power num2
# 8 // 2 power 3
result1 = num1 >> num2 
print("Result right shift is:", result1)

#Not all numbers will retrive
number = result1 <<num2 
print("number is: ", number) # we will get num1 back

# multiplying by 2 power num2
# 8 * 2 power 3
result2 = num1 << num2
print("Result left shift is: ", result2)

number = 11 
result = number >> 2
print(number, ">> 2 is", result)

# 11
# 0 0 0 0 1 0 1 1
# >> 2
# _ _ 0 0 0 0 1 0 -> 2