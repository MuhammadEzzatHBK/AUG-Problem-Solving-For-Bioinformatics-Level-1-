# Read a given string, change the character at a given index and then print the modified string.
    # The first line contains:
        # string sequence: the string to change
    # The second line contains:
        # int position: the index to insert the character at
        # string character: the character to insert
    # he index and the character separated by a space.
# Input: 'abracadabra'
#        'k' 5
# Output: 'abrackdabra'

# code
sequence = input()
idx, char = input().split()
newSequence = sequence[:int(idx)] + char + sequence[int(idx)+1:]
print(newSequence)
