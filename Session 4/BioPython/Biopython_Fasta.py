from Bio import SeqIO
from Bio.Seq import Seq

for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    sequence = Seq(seq_record.seq.__str__())
    print('A:', sequence.count('A'), ', T:', sequence.count('T'), ', G:', sequence.count('G'), ', C:', sequence.count('C'))
    print('Length is: ', len(seq_record), '\n')