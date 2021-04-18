
@auther nouran ahmed ibrahim


ListOfStrings = ["Mohamed", "Ayman", "Ahmed", "Ziad"]
ListOfBoolean = [True, False]
ListOfNumbers = [1, 5, 3 ,3]
ListOfLists = [[2, "UGA"], [1, "AUG"], [2, "UAG"],  []]

# '''
# order the list from smaller to the greater
ListOfBoolean.sort()
ListOfStrings.sort()
ListOfLists.sort()
ListOfNumbers.sort()

print(ListOfNumbers)
print(ListOfStrings)
print(ListOfBoolean)
print(ListOfLists)

# '''
# get num of items in the list
print("List length : ", len(ListOfNumbers))

# get the number of occurrences of a certain item
print("The number of appearance of num 3 : ", ListOfNumbers.count(3))

# get the first appearance of a certain item in the list
print("The first appearance of num 3 : ", ListOfNumbers.index(3))

# reverse list
ListOfStrings.reverse()
print(ListOfStrings)

# '''
