from Bio.Seq import Seq
from Bio.SeqUtils import GC

seqDna = Seq("GATCGATGGGCCTAT")
seqRna = Seq("GAUCGAUGGGCCUAU")

print(seqDna)
print(seqDna.complement())
print(seqDna.reverse_complement())

print('\nNumber of Sequences: ', len(seqDna), '\n')

for index, letter in enumerate(seqDna):
    print("%i -> %s" % (index, letter))

print('\nIndex [5] of Sequence is: ', seqDna[5], '\n')

print('num of (A) is: ', seqDna.count('A'))
print('num of (T) is: ', seqDna.count('T'))
print('num of (G) is: ', seqDna.count('G'))
print('num of (C) is: ', seqDna.count('C'))

print('\nPercentage of {GC} is: ', GC(seqDna), '\n')

print(seqRna)
print(seqRna.complement_rna())
print(seqRna.reverse_complement_rna())