# String in Action
# Textual Data Type

name = 'John'
cafe_name = "John's Cafe"

# Multi Line String
message = """Hi
How Are you..
This is John from John's Cafe
"""

# Raw String -> Accepts special characters as data
# Regular Expression uses Raw String 
cafe_name = r'John\'s \nCafe'

print(name)
print(cafe_name)
print(message)

# Properties
"""
    Indexing
    Negative Indexing
    Slicing
    Concatenation
    Multiplicity
    Membership Testing
"""

quote = "search the candle rather than cursing the darkness"
print("1. HashCode of Quote:", id(quote))

print(quote[1])
print(quote[-1])
# Indexing and Negatuve indexing works
print(quote[-8:])
# Slicing works

quote = quote + "\n" + "Be Exceptional\n"
print(quote)
# Concatenation works
print("2. HashCode of Quote:", id(quote))

data = quote * 3
print("`````````````````")
print(data)
print("`````````````````")
# Multiplicity works

print("the" in quote)
# Membership testing works

# Real-time application of Membership Testing
email = input("Enter Your Email: ")
if "@" in email and "." in email:
    print("Email is Well Formed:", email)
else:
    print("Email is NOT Well Formed:", email)


contacts = ["john", "jennie", "kia", "joe", "jackson", "anna", "sia"]
search = input("Enter Search keyword: ")
for contact in contacts:
    if search in contact:
        print(contact)