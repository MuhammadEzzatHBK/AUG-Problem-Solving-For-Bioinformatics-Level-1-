from Bio.Seq import Seq

def cMers(tSeq, k):
    kFreq = {}

    for x in range(0, len(tSeq) - k + 1):
        kMer = tSeq[x : x+k]

        if kMer in kFreq:
            kFreq[kMer] += 1
        else:
            kFreq[kMer] = 1
    return kFreq


f = open('dataSeq.txt', 'r')
mySeq = Seq(f.read())

cKmer = cMers(mySeq, 3)
print(cKmer)