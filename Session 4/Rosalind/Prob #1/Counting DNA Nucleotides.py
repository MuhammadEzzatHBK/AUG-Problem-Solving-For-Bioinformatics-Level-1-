




#Correct Answer #1
'''
#using Bio Library
from Bio.Seq import Seq

dataFile = open('rosalind_dna.txt', 'r')
dnaSeq = Seq(dataFile.read())

print(dnaSeq.count('A'), dnaSeq.count('C'), dnaSeq.count('G'), dnaSeq.count('T'))

dataFile.close()
'''

#Correct Answer #2
'''
def countNucleotides(seq): #Function
    mySeq = { #Dictionary
        "A": 0, "C": 0, "G": 0, "T": 0
    }

    for x in seq:
        mySeq[x] += 1

    return mySeq


dataFile = open('rosalind_dna.txt', 'r')

fileResult = countNucleotides(dataFile.read())
print(' '.join([str(val) for key, val in fileResult.items()]))

dataFile.close()
'''