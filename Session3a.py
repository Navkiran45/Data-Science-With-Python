#conditional operators
# ==, !=, >, <, >=, <=

cab_fare = 500
e_wallet = 200
result = e_wallet >= cab_fare
print("Can I book the cab?", result)
print(type(result))

email = input("Enter Email: ")
password = input("Enter Password: ")

print("Is Login Success ??")
result = (email == "navkiran@example.com") and (password == "aa@123")
print(result)

otp = 3027
user_otp = int(input("Enter OTP Recieved: "))
print("Is OTP Correct??", otp == user_otp)

#Membership Testing
# is, is not

a = 10
b = 10
print(a == b) #True
print(a is b) #True
print(a is not b) #False

#Difference between == and is 