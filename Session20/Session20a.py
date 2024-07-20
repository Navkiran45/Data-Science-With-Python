# Strings are IMMUTABLE -> THEY CANNOT BE CHANGED
# If you want to do changes, make a new string

quote = "be exceptional"
print("HashCode of quote is:", id(quote))
s1 = quote.upper()
print("1. Quote is:", quote)
print("1. HashCode of quote is:", id(quote))

s2 = quote.lower()
print("2. Quote is:", quote)
print("2. HashCode of quote is:", id(quote))

print("s1 is:", s1)
print("s2 is:", s2)

s3 = quote.capitalize()
print("s3 is:", s3)

s4 = quote.title()
print("s4 is:", s4)

quote = "Be Exceptional"
s5 = quote.swapcase()
print("s5 is:", s5)


password = "  hello  "
print(password, len(password))
p1 = password.strip()
print(p1, len(p1))
# strip() removes from starting and ending

data = "00000382900"
print(data.strip("0"))
print(data)

amount = 35.540000
new_amount = float(str(amount).strip("0"))
print(new_amount, type(new_amount))

quote = "search the candle rather than cursing the darkness"
# s1 = quote.replace("t", "k")
s1 = quote.replace("the", "hello")
print(quote)
print(s1)

message = "No Internet Connection"
print(message)
print(message.center(50))
print(message.ljust(50))  #left justification
print(message.rjust(50))  #right justification

amount = 545
data = str(amount).zfill(8)
print("data is:", data)

quote = "search the candle rather than cursing the darkness"
idx1 = quote.find("the") #find() finds the index of the starting character
idx2 = quote.find("dark")
print("idx1:", idx1)

print(quote[idx1:idx1+3]) # print(quote[7:10])
print(quote[idx2:])

idx3 = quote.rfind("the") #rfind() from right side 
print(idx3)

# we can use find as well as index function for indexing
print(quote.index("the"))
print(quote.rindex("the"))