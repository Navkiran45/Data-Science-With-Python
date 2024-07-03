"""
def add(num1, num2):
    sum = num1 + num2 
    return sum

compute = add

def compute(num1, num2):
    return num1 + num2 * 2

square = compute

result = square(num1 = 10, num2 = 2)
print(result)

result1 = add(num1=10, num2=2)
print(result1)
"""
# args and kwargs
# args -> variable number of 
def add(*args):
    print(args)
    print(type(args))
    data = list(args)
    print(data)
    print(type(data))

add(10, 20, 30, 40, "hi", "john")

#keyword arguments
def numbers(**kwargs):
    print(kwargs)
    print(type(kwargs))
numbers(a=10, b=20, c=40)

def fun(*args, **kwargs):  # **kwargs, *args -> will give error!
    print(args)
    print(kwargs)

fun(10, 20, 30, 40, 50, "hi", a=30, b=90, f= 40)