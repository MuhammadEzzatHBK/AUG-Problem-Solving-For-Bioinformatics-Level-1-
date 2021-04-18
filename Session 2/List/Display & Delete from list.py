@auther nouran ahmed ibrahim

List = [1, "Hallo", [2, "inner list"], "Hello", True]

# print the whole list
print(List)

# print the whole list reversed
print(List[:: -1])   # don't change order permanent


# print range from the list
print(List[0:2])
print(List[:2])
print(List[2:])

# print specific index
print(List[2][1])
print(List[3])
print(List[-1])


# remove the first appearance
List.remove("Hallo")
print(List)

popWord = List.pop()
print(popWord)
print(List)

List.clear()
print(List)
