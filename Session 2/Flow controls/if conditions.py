@auther nouran ahmed ibrahim

isTired = False
sleepWell = True

# isTired == true
if isTired or sleepWell is False:
    willSleep = True
    print("will sleep")
else:
    willSleep = False
    print("will not sleep")

# change salary based on jop type
jop = 'Programmer'

if jop in ["Programmer", "Engineer"]:
    salary = 8000
else:
    salary = 5000
print("The salary is : ", salary)

# weather situation

result = 30
if result <= 15:
    print("cold")
elif result <= 30:
    print("sunny")
else:
    print("hot")

# short if else
print("hallo") if 5 > 3 else print("bye")


# print GPA

result = 80

if result >= 50:
    if result >= 89:
        print("A")
    elif result >= 75:
        print("B")
    else:
        print("C")
else:
    print("Failed")
