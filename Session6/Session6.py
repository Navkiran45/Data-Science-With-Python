#IMPORTANT
#Recurssion
def print_number(number):
    print(number)

    if number < 11:
        print_number(number+1) #Function calling itself again and again
print_number(1)
