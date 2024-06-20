def square(num):
    print("1. num is:", num, id(num)) #10
    num *= num # num = num*num
    print("2. num is: ", num, id(num)) #100

#Functions exist in memory
print("Square: ", square) #Hashcode and name of function

number = 10
print("A. number is: ", number, id(number)) #10
square(number)
print("B. number is: ", number, id(number)) #10

print("-------------------------")

def square_of_numbers(nums):
    print("1. nums is: ", nums, id(nums)) 
    for idx in range(0, len(nums)):
        nums[idx] = nums[idx]*nums[idx]
    print("2. nums is: ", nums, id(nums))

numbers = [10,20,30,40,50]
print("A. numbers is: ", numbers, id(numbers))
square_of_numbers(numbers)
print("B. numbers is: ",numbers, id(numbers))

#MVC is not changing, but SVC in MVC are changing 