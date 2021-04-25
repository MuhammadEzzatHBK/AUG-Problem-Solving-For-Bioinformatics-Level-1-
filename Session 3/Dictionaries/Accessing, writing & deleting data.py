my_dictionary = {
    'type': 'Fruits',
    'name': 'Apple',
    'color': 'Green',
    'available': True,
    'number': 25
}

print(my_dictionary)
print(my_dictionary['name'])
# searching with wrong key
print(my_dictionary['weight'])

###############################################################

# printing keys and values
for d in my_dictionary:
    print(d, my_dictionary[d])

# printing values direct
for data in my_dictionary.values():
    print(data)

###############################################################

# modify a value
my_dictionary['color'] = 'Red'
print(my_dictionary)

###############################################################

# inserting new item
my_dictionary['weight'] = '5k'
print(my_dictionary)

###############################################################

# deleting an item
del my_dictionary['weight']
print(my_dictionary)

###############################################################
