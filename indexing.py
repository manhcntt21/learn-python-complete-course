# index operator []: gives access to a sequence's element (str, list, tuples)

name = "Manh Do!"

# check first character of string is lowercase
if name[0].islower():
    name = name.capitalize()

print(name)

first_name = name[:4].upper()
last_name = name[5:-1].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)