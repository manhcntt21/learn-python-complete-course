# filter() : creates a collection of elements from an iterable for which a function return true

# filter(function, iterable)

friends = [
    ('Michael', 60),
    ('Lincoln', 33),
    ('T-Bag', 36),
    ('Secure', 20),
    ('Ross', 10),
    ('Well', 15),
]

age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age, friends))
print(drinking_buddies)