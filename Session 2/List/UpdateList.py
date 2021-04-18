
@auther nouran ahmed ibrahim

List1 = ["World"]
List2 = []

List2.append("Hallo")
print("List2 : ", List2)

List2.insert(0, 1)
print("List2 : ", List2)

# List2 += List1
List2.extend(List1)
print("List2 : ", List2, "\n")

# Shadow copying
List1 = List2.copy()
List2[0: 2] = [2, "Bye"]
print("List1", List1)
print("List2", List2, "\n")

# copy

List1 = List2
List2[0] = 3
print("List1" + str(List1))
print("List2" + str(List2) + "\n")

List1[0] = 4
print("List1" + str(List1))
print("List2" + str(List2) + "\n")
