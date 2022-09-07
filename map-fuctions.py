# map: applies a function to each item in an iterable (list, tuple, etc)
# map(function, iterable)

store = [
    ('shirt', 20.00),
    ('pants', 25.00),
    ('jackets', 50.00),
    ('socks', 10.00),
]

# convert $ to euros
to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)
#                 function  iterable
store_euros = list(map(to_euros, store))
# or use for loop
print(store_euros)
store_dollars = list(map(to_dollars, store))
print(store_dollars)