# Read from fasta :
from Bio import SeqIO

fasta_sequences = SeqIO.parse(open('input_file.fasta'), 'fasta')
for seq_record in fasta_sequences:
    print('id: ', seq_record.id)
    print('reduced seq:', repr(seq_record.seq))
    print('total seq:', seq_record.seq)
    print('length: ', len(seq_record), '\n')
