# Condition: You can apply promo code if and only if min amount is 500
promo_code = "GET200"
min_amount = 500

amount = float(input("Enter Your Amount: "))

# Conditional Construct: if-else
if amount> min_amount:
    print("You can apply promo code", promo_code)
    amount -= 200
    print("Promo Code Applied SUccessfully. Please pay: ", amount)
else:
    print("You cannot apply promo code", promo_code)
    print("Add items worth", (min_amount - amount), "more..")

print("-------------------------")

# Promo Code: ZOMATO
#Condition1: more than 249
#Condition2: 50% off upto 150

amount = float(input("Enter amount: "))
promo_code = input("Enter Promo Code: ")

if promo_code == "ZOMATO":
    print("Promo Code Valid")

    if amount > 249:
        print("Promo Code ZOMATO applied..")

        discount = 0.50 * amount

        if discount>= 150:
            discount = 150 

        amount -= discount
        print("Discount: ", discount)
        print("Please Pay:", amount)
    else:
        print("Amount is low")

else:
    print("Promo Code Invalid")