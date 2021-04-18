sortedList = []
List = [3, 1, "hi", "bye"]


def sortIntegers():
    sub_List = []
    for item in List:
        if type(item) == int:
            sub_List.append(item)
    else:
        sub_List.sort()
        sortedList.extend(sub_List)



def sortStrings ():
    sub_List = []
    for item in List:
        if type(item) == str:
            sub_List.append(item)
    else:
        sub_List.sort()
        sortedList.extend(sub_List)


sortIntegers()
sortStrings()
print(sortedList)

