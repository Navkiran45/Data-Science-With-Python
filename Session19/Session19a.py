#Functions on Lists
numbers = list(range(10, 101, 10))
# numbers = tuple(range(10, 101, 10))
print("numbers is:", numbers)
print("numbers type is:", type(numbers))

numbers.append(99)
numbers.append(77)
numbers.append(103)
numbers.append(11)

print("numbers is:", numbers)
print("Len is:", len(numbers))
print("Sum is:", sum(numbers))
print("Min is:", min(numbers))
print("Max is:", max(numbers))
print("Avg is:", sum(numbers)/len(numbers))

# result = tuple(reversed(numbers))
result = list(reversed(numbers))
print("result is:", result)

names = ["john" , "Jennie", "Abel"]
result = names.sort()
print(result)
print("Min is: ", min(names))
print("Sum is: ", sum(names))

# Functions on Tuples
numbers1 = (40, 90, 50, 30, 80)
#numbers.append(99)
# append doesnt work in tuple

#numbers.sort()
#print("Sort is:" , numbers)
# sort doesnt work on tuple

print(max(numbers1))
print(min(numbers1))

#numbers.remove(90)

#numbers.pop(99)
#numbers.insert(2,78)
#numbers.append(87)

#numbers.clear()