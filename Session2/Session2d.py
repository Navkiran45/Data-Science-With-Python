#ADD TO CART

cart = []
price = []
quantity = []

menu = {
    "noodles": 200,
    "burger": 60,
    "momos": 80,
    "pizza": 300,
    "spring roll": 90,
}

print("--------------------")
print("Welcome to Foodies..")
print("--------------------")
print("Food Menu")
print(menu)
print("--------------------")

while True:
    item = input("Enter food item to add in cart or 0 to quit: ")

    if item == "0":
        break

    qty = int(input("Enter Quantity for item: "))
    quantity.append(qty)
    cart.append(item)

    price.append(menu[item]*qty)

print("Item(s) in cart are:")
print(cart)
print("Quantity: ")
print(qty)
print("Prices are: ")
print(price)
print("Items in cart are:", len(cart))
print("Amount to Pay:", sum(price))