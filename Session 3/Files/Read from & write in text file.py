# Reading from a file:
myFile = open('input.txt', 'r')
# using read()
print(myFile.read())

# using readline()

print(int(myFile.readline()) * 2)
print(myFile.readline())

# using readlines()
print(myFile.readlines())

# using for...in

for line in myFile:
    print(line)

myFile.close()

################################

# Writing in a file:

# Write mode
myFile = open('output1.txt', 'w')
myFile.writelines(['first sentence!', 'second sentence!'])

myFile.writelines(['first sentence!', '\n',  'second sentence!'])

myFile.close()

# Append mode
myFile = open('output2.txt', 'a')
myFile.writelines(['\nfirst sentence!', '\n',  'second sentence!'])
myFile.close()

################################

# Reading from or writing in the same file:
myFile = open('mixed.txt', 'r+')
print(myFile.read())
myFile.writelines(['\nfirst sentence!', '\n',  'second sentence!'])
myFile.close()
