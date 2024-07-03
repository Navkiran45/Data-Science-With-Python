# MULTI VALUE CONTAINERS
"""
    Sequences:
        Tuple
        List
        String
    Set
    Dicttionary
"""
"""
Properties:
1, Indexing
2. Negative Indexing
3. Slicing
4. Concatenation
5. Multiplicity
6. Membership Testing
"""

# 1 D List
# Indexing
        #  0   1  2
        #  -3  -2 -1
my_data = [10,20,30]

# 2 D List
numbers = [
    [10,20,30], # 0  -3
    [30,40,50], # 1  -2
    [60,70,80]  # 2  -1
]

# 3 D List
large_data = [
    [
    [10,20,30],                     # 0   -2
    [30,40,50], 
    [60,70,80]  
    ],
    [
    [110,210,310],                  # 1     -1
    [320,420,520], 
    [630,730,830]  
    ]
]
print(my_data[0])
print(my_data[-1])
print(len(my_data))

print(numbers[0])
print(numbers[-1])
print(len(numbers))

print(large_data[0])
print(large_data[-1])
print(len(large_data))

print(large_data[1][0][0])
print(large_data[-1][-3][-3])

# Indexing will work on Lists and Tuples {not on Sets and Dictionary}

# String
name = "John's Cafe"  #Commonly used " "
name = 'John\'s Cafe' # When using single quotes, difficult to have 's words but can use \ to prevent error
name = """John's Cafe 
Welcome to Cafeteria
Today's Menu:
Burger
Coffee"""
# """ """ is efficient as we can have multi lines
print(name)
print(name[0])
print(name[-1])
print(name[-2])

# SLICING
data = list(range(10,101,10))
print("Data is ")
print(data)

print("data[0:3]", data[0:3]) # 0 inclusive, 3 exclusive ; will run till 2
print("data[3:7]", data[3:7]) # 3 inclusive, 7 exclusive ; will run till 6
print("data[5:]", data[5:])   # will run from 5 to last index
print("data[:4]", data[:4])   # will run from 0 index to 3 index, 4 not inclusive

print("data[:-5]", data[:-5]) # as it is negative, will run from -1(last index) to -6, -5 not inclusive
print("data[-5:-2]", data[-5:-2]) # will run from -5 to -3, -2 not inclusive

# Slicing on Strings
work = "Artifical Intelligence Expert"
print("work[0:3]",work[0:3])
print("work[3:6]",work[3:6])
print("work[-3:-10]",work[-3:-10])

# Slicing works on Lists, Tuples, Strings

# Concatenation
data1 = [10,20,30]
data2 = [40,50,60]

data3 = data1 + data2
print(data3)

# Multiplicity
data4 = data1 * 2
print(data4)

prices = [100,500,700,300]
prices1 = prices * 2
print(prices1)

#Membership Testing
print(10 in prices)      # False
print(10 not in prices)  # True

quote = "Search the candle rather than cursing the darkness"
print(quote[6])
print(quote.split(" "))

# Properties On Sets

prop = { 20, 30, 50, 60}
prop1 = { 70, 80}
# print(prop[1])
# print(prop[-1])
# Indexing doesnot work

#print("prop [0:3]", prop[0:3])
#Slicing doesnot work

#prop3 = prop + prop1
#print(prop3)
# Concatenation doesnot work

#prop2 = prop1 * 2
#print(prop2)
# Multiplicity doesnot work

print(20 in prop)
# Membership Testing is working on Sets

# Properties On Dictionaries

student = { "roll no.": 1,
           "name": "John",
           "age": 20,
           "gender": "male",
           }
#print(friends[1])
# Indexing doesnot work as keys are there so
print("student[age]: ",student["age"] )

#Slicing doesnot work

#Membership testing works on Dictionaries