
@auther nouran ahmed ibrahim

List = ['a', 1, "b", 2, 'c', 'd']

# display all items in list
for item in List:
    print(item)

# find num  of small char in list
countChar = 0

for item in List:
    if str(item).isalpha():   # convert all items to String then check if it char or not
        countChar += 1

print("number of chars : ", countChar)

# '''
# find element index in the list
for index in range(len(List)):
    if List[index] == "b":
        print("b appeares in : ", index)
        break
# '''
