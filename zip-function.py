# zip(*iterable): aggregate elements from two or more iterables (list, tuple, set, etc)
# creates a zip object with paired elements stored in tuple for each element

user_name = ['Dude', 'Bro', 'Mister']
pass_word = ['p@assword', 'abc123', 'guest']
login_date = ['1/1/2021', '1/2/2021', '1/3/2021']

users = zip(user_name, pass_word)  # result, each element is a tuple
print(type(users))
# convert zip to list
users = list(users)
print(users)
# convert zip to list to dict
users = dict(users)
print(users)
# zip three iterable
users2 = zip(user_name, pass_word, login_date)
print(list(users2))
