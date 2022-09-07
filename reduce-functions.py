# reduce(): applies a function to an iterable and reduce it to single cumulative value
# perform function on first two elements and repeats process until 1 value remains

# reduce(function, iterable)

import functools
letter = ['H', 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x, y: x + y, letter)
# ['HE', 'L', 'L', 'O']
# ['HEL', 'L', 'O']
# ['HELL', 'O']
# ['HELLO']
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)