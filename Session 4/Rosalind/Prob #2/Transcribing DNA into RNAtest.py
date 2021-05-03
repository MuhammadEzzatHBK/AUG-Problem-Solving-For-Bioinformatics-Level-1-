




#Correct Answer
'''
#Using String Replace
dataFile = open('rosalind_rna.txt', 'r')

readFile = dataFile.read()
dnaTOrna = readFile.replace('T', 'U')

print(dnaTOrna)

dataFile.close()
'''