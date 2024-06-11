#DICTIONARY -> Final and most important and mostly used container in CS

friends = {"jj": "john", "je": "jennie", "ji": "jim"}
print(friends, type(friends), id(friends))
print(friends["jj"])

my_friends = { 1: "Call", 2: "Message", 3: "Get a Callback"}

instagram = {
    "navkiran": {"mayank", "ishpreet", "harjot", "devesh"},
    "mayank": {"navkiran", "ishpreet", "avleen", "devesh"}
}
print(instagram["navkiran"])
print(instagram["mayank"])

print(instagram["navkiran"] & instagram["mayank"])

