my_dictionary = {'type': 'Fruits', 'name': 'Apple', 'color': 'Green', 'available': True, 'number': 25}

# copying
new_dic = my_dictionary.copy()
my_dictionary['color'] = 'Red'
new_dic['available'] = False
print(my_dictionary)
print(new_dic)

# having same reference
new_dic = my_dictionary
my_dictionary['color'] = 'Red'
new_dic['available'] = False
print(my_dictionary)
print(new_dic)

###############################################################

# removing an item
item = my_dictionary.pop('available')
print(item)
item = my_dictionary.popitem()
print(item)
print(my_dictionary)

###############################################################

# getting an item
value = my_dictionary.get('number')
print(value)
value = my_dictionary.get('num', 'not found')
print(value)

# getting all items
items = my_dictionary.items()
print(items)

# getting keys names
keys = my_dictionary.keys()
print(keys)

# getting values
values = my_dictionary.values()
print(values)

###############################################################

# combining two dictionaries
dict1 = {'name': 'Ahmed', 'job': 'programmer'}
dict2 = {'salary': 7500, 'hours': 7}

dict1.update(dict2)
print(dict1)
print(dict2)

###############################################################
