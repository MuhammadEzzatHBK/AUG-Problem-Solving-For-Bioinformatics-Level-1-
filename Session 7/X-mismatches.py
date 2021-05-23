from operator import itemgetter

def extract_kmers(sequence, k):
    kmers = []
    kmer = ""

    for i in range(len(sequence) -k+1):
        kmer = sequence[i]
        for j in range(1,k):
            kmer += sequence[i+j]
        kmers.append(kmer)
    return kmers


def hamming_distance(seq1, seq2):
    distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            distance += 1
    return distance


def CountX(seq, k, x):
    kmers = extract_kmers(seq, k)
    unique_kmers = list(set(kmers))
    counter = {unique_kmer:0 for unique_kmer in unique_kmers}
    for unique_kmer in unique_kmers:
        for kmer in kmers:
            if hamming_distance(unique_kmer, kmer) <= x:
                counter[unique_kmer] += 1
    return counter


sequence = 'ATGCGAATGTGAATGCCAATGACTATG'

raw_dictionary = CountX(sequence, 3, 1)
sorted_dictionary = sorted(raw_dictionary.items(), key = itemgetter(1))

print(sorted_dictionary, '\n')
print(sorted_dictionary[-1])