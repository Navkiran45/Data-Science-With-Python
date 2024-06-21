"""
idx = int(input("Enter number of elements: "))
for i in range(0,idx):
    input(("Enter element: "))


list = [20,10,40,30]
n = len(list)
for i in range(0, n-1):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
    
for i in range(0, n-1):
    print(list[i])
"""

def bubble_sort(data):
    for i in range(0,len(data)-1):
        print("i is: ",i)
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                print("Swapping {} with {}".format(data[j], data[j+1]))
                #Swap Operation
                data[j], data[j+1] = data[j+1], data[j]
        print()   

numbers = [10, 30, 50, 20, 40]
print("Unsorted numbers: ")
print(numbers)
bubble_sort(numbers)
print("Sorted numbers:")
print(numbers)
