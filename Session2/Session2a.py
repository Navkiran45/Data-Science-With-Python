#SETS #UNIQUENESS
#unordered coz it uses hashing
#doesn't support duplicay 

numbers = {10, 20, 11, 22, 55, 57}
print(numbers, type(numbers), id(numbers))

john_friends = { 'joe', 'jim', 'fionna', 'harry', 'kim', 'joe'}
sia_friends = { 'joe', 'george', 'fionna', 'leo', 'jack', 'ben'}
print(john_friends)
print(sia_friends)

mutual_friends = john_friends & sia_friends
print(mutual_friends)
#set doesnot support indexing. 
#it works on hashing, hence we cannot get the data from set.