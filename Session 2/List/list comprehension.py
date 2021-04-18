
@auther nouran ahmed ibrahim

requirements = ["apple", "milk", "kiwi", "meat"]

# copy the old list
newRequirements = [x for x in requirements]
print(newRequirements)

# newList contain all items that contain char a
newRequirements = [x for x in requirements if "a" in x]
print(newRequirements)

newRequirements = ['no-thing' for x in requirements]
print(newRequirements)

# add chars expect U and replace it with T
newSequence = [x if x != "U" else "T" for x in "AGACCGCUUA"]
print(newSequence)

# numbers that divisible by 2 and 3 from 10 to 51
print("Numbers that divisible by 2 and 3 from 10 to 100 :\n", [i for i in range(10, 52) if i % 3 == 0])
