@auther nouran ahmed ibrahim

num = 0

# while loop
# print numbers to 15

while num <= 15:
    print(num)
    num += 1
else:  # will execute after end the loop if there is no break
    print("Num value at the end is : ", num)

# print all number that divide 4
num = -5

while num <= 5:
    if num == 0:   # can use nested if or and
        num += 1
        continue
    if 4 % num == 0:
        print(num, end=" ")

    num += 1

# find num that divisible by 2 , 3 5
num = 1

while num <= 100:
    if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
    num += 1

# For loop

# print numbers from 0 to 9
for x in range(10):   # 0, 1...10
    print(x)

# count number of A & G in DNA
countA = 0
countG = 0

for char in "AGAACTC":
    if char == 'A':
        countA += 1
    elif char == 'G':
        countG += 1

print("Number of A : ", countA, " & G : ", countG)


# Nested Loop

for row in range(4):
    for col in range(3):
        print(col, end=" ")
    print()

# Draw square composed of letters
for row in range(4):
    for char in range(ord('A'), ord('E')):  # ord get the ASCII code of a character
        print(chr(char), end=" ")  # chr get the character encoded by an ASCII code
    print()

# Draw inverted isosceles right-angle triangle
for row in range(5, 0, -1):  # decrement row value by 1
    for col in range(1, row + 1):
        print(col, end=" ")  # print col value and space without printing new line
    print()

# '''
