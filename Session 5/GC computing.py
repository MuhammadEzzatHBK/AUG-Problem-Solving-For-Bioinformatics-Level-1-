from Bio import SeqIO


def calcGC(seq=""):
    GCCount = seq.count('C')
    GCCount += seq.count('G')

    return (GCCount / len(seq)) * 100


def findMax(Seqs):
    mx = ["", -1]
    for currentId in Seqs:
        if mx[1] < Seqs[currentId]:
            mx[1] = Seqs[currentId]
            mx[0] = currentId
    return mx


Data = SeqIO.parse(open("C:/Users/AAAAA/Desktop/input.txt"), format="fasta")
GCContent = {}

# calc GCContent for all sequences

for currentSequence in Data:
    GCContent[currentSequence.id] = calcGC(currentSequence.seq)

maxGC = findMax(GCContent)
print(maxGC[0])
print(maxGC[1])
