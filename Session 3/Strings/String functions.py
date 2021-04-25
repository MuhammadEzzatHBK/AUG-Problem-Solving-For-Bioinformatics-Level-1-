# removing characters from string poles
text1 = '   apples and oranges   '
print(text1.strip())

text2 = '...+...lemons and limes...-...'
# Here we strip just the "." characters
print(text2.strip('.'))

# Here we strip both "." and "+" characters
print(text2.strip('.+'))

# Here we strip ".", "+", and "-" characters
print(text2.strip('.+-'))

###############################################################

# searching for character
s = 'here we go'
print(s.find('r'))
print(s.find('z'))

###############################################################

# connecting strings
strings = ['coding', 'makes', 'me', 'happy']
s = '_'.join(strings)
print(s)

###############################################################
