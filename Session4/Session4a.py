#LINEAR SEARCH 

instagram_user_names = [ "john.j", "fionna", "harry_h", "leo.32", "ben_a"]
names = ["John Jackson", "Fionna Flynn", "Harrison", "Leonardo", "Bennethan"]

user_name = input("Enter username to search: ")
"""
# While Loop
idx = 0

while idx < len(instagram_user_names):
    if user_name == instagram_user_names[idx]:
        print("Name is: ", names[idx])
        break
    idx +=1
"""
#For Loop

flag = False
for idx in range(0, len(instagram_user_names)):

    print("Check", user_name, "with", instagram_user_names[idx])
    if user_name == instagram_user_names[idx]:
        print("Name is: ", names[idx])
        flag = True
        break
if flag == False:
    print(user_name , "not found.")