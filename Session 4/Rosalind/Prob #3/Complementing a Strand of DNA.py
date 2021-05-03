




#Correct Answer
'''
#using Bio.Seq Library
from Bio.Seq import Seq

dataFile = open('rosalind_revc.txt', 'r')

dnaSeq = Seq(dataFile.read())
dnaComplement = dnaSeq.reverse_complement()

print(dnaComplement)

dataFile.close()
'''