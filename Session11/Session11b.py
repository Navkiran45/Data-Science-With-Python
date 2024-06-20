file = open("customer.csv" , "r")
#data = file.read() 

lines = file.readlines()

print("Customer Data")
print(lines)

for i in range(len(lines)):
    print(lines[i])