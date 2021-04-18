@auther nouran ahmed ibrahim

students = []


def greeting():
    print("Welcome")


def displayStudentsInfo():
    for student in students:
        print("Student name", students[0])
        print("Student academic year", students[1])
        print("Student grade", students[2])


def addStudent(*info):
    students.append([info[0], info[1], totalGrades(info[2])])


def totalGrades(grades):
    total = 0
    for currentGrade in grades:
        total += currentGrade
    return total


def readStudentInfo():
    grades = []
    print("Enter new student info")
    name = input("Enter student name : ")
    year = input("Enter student academic year : ")
    grades.append(input("Enter subject 1 grade"))
    grades.append(input("Enter subject  grade"))
    addStudent(name, year, grades)


greeting()

# what will happen if print function has no return
print(greeting())
readStudentInfo()
displayStudentsInfo()
