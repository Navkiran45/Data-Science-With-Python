# INDENTATION: PEP (PYTHON ENCHANCEMENT PROPOSAL)
"""
    ZOMATO: 20% oFF
        min value: 300
    BINGO : 50% off
        min valu: 500
        max discount: 100
"""

# if-else -> Workflows
promo_code = input("Enter promo code:")
amount = float(input("Enter Amount: "))

if promo_code == "ZOMATO":
    print("ZOMATO can be applied..")

    if amount > 300:
        discount = 0.20 * amount
        print("ZOMATO Applied Successfully. You got Discount of: ", discount)
        print("You can pay:", amount - discount)
    else:
        print("Amount is less. Please add items worth", (300- amount), "more")

elif promo_code == "BINGO":
    print("BINGO can be applied..")
    if amount > 500:
        discount = 0.50 * amount

        if discount > 100:
            discount = 100

        print("BINGO Applied Successfully. You got Discount of: ", discount)
        amount -= discount
        amount = amount + 0.18*amount
        amount += 16.5 #delievery fee
        print("You can pay: \u20b9", amount - discount)
    else:
        print("Amount is less. Please add items worth", (500- amount), "more")

else:
    print("Invalid Promo Code")

#USING UNICODES

name = {"\u0A28\u0A35\u0A3F\u0A15\u0A30\u0A28 \u0A4C\u0A15\u0A30"}
print(name)