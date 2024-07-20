# SETS
a = {1,2,3,4,5}
b = { 4,5,6,7,8}

"""c = a + b
print("a is: ", c)"""
# doesnot concatenate in Sets

d = a - b
print("d is: ", d)

e = a ^ b
print("E is: ", e)

f = a | b
print("F is : ", f)
# using OR for concatenation

a.clear()
print("a is", a)
print("Length of a is: ", len(a))

#Create an Empty Set
my_set = set()
my_list = []
my_dict = {}
my_tuple = ()
# no benefit of empty tuple coz we cant modify it 

# DICTIONARY/Map/JSON

my_data = {
    101: "john",
    201: "Jennie",
    501: "Sia",
    901: "Joe",
    99: "Kim"
}

print("my_data", my_data)

print(len(my_data))
print(min(my_data))
print(max(my_data))
print(sum(my_data))
# min, max, sum is working on keys

my_data = {
    "jo": "john",
    "je": "Jennie",
    "si": "Sia",
    "jo": "Joe",
    "ki": "Kim"
}

print("my_data", my_data)

print(len(my_data))
print(min(my_data))
print(max(my_data))
#print(sum(my_data))
# sum works only for integer keys

covid_data = {
    "usa" : {"Active":50, "Serious":30, "Recovered": 10},
    "india" : {"Active":50, "Serious":30, "Recovered": 10},
    "uk" : {"Active":50, "Serious":30, "Recovered": 10},
    "italy" : {"Active":50, "Serious":30, "Recovered": 10},
    "brazil" : {"Active":50, "Serious":30, "Recovered": 10},
}

