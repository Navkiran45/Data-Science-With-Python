def get_max(data, length):
    # data, length belongs to get_max frame
    if len(data) == 1:
        return data[0]
    else:
        previous = get_max(data, length-1)
        current = data[length-1]
    
    if previous > current:
        return previous
    else:
        return current
        
#numbers, max belongs to main frame
numbers = [10, 20]
max = get_max(numbers, len(numbers))
print("Max is: ", max)