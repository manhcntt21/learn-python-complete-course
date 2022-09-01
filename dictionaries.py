# dictionary: a changeable, unordered collection of unique key:value pairs
# fast because they use hashing, allow us to access a value quickly

capitals = {
    'USA': 'Washington DC',
    'Vietnam': 'Hanoi',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

print(capitals)
print(capitals['Vietnam'])
# a key not exist
# KeyError: 'Germany'
# print(capitals['Germany'])

# check key before
print(capitals.get('Germany'))
# None

# print all keys
print(capitals.keys())

# print all value
print(capitals.values())

# print both values and keys
print(capitals.items())

# iteration with dictionary
for key, value in capitals.items():
    print(key, value)

# update
# add new element into dictionary
capitals.update({'Germany': 'Berlin'})
print(capitals)

# update exist element
capitals.update({'USA': 'Las Vegas'})
print(capitals)

# pop element
capitals.pop('Germany')
print(capitals)

# clear
capitals.clear()
print(capitals)

