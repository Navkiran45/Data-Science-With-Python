#Create Statement
promo_code1 = "ZOMATO40"
print(promo_code1, type(promo_code1), id(promo_code1))

#Reference Copy Operation
promo_code2 = promo_code1
print(promo_code2, type(promo_code2), id(promo_code2))

#DELETE
del promo_code1
print(promo_code2, type(promo_code2), id(promo_code2))

#Below statement will throw error
#print(promo_code1, type(promo_code1), id(promo_code1))
