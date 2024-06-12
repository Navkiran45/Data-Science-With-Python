"""
    Another Brick in the Wall
    Who placed, the last brick and how many?

    Mr. John -> Requirement | create a wall with 13 bricks
                         BRICKS
    jack: 1             1
    joe: 2              3

    jack:2              5
    joe: 4              9
    
    jack: 3             12
    joe: 6              13
    
    joe -> last brick
        1 brick
"""

bricks = int(input("number of bricks:"))
sum = 0
idx = 1
joe = 1
while sum< bricks:
    print("joe inserted: ", joe)
    john = 2*joe
    print("John inserted:", john)
    if sum + joe >= bricks:
        sum += joe
        last_person = "Joe"
        last_bricks = joe
        break
    
    sum += joe
    if sum + john >= bricks:
        sum += john
        last_person = "John"
        last_bricks = john
        break
    sum += john
    print("Sum: ", sum)
    joe +=1
print("We need total bricks", bricks, "so in last iteration bricks inserted were: ",last_bricks - (sum -bricks), "which was inserted by: ", last_person)
