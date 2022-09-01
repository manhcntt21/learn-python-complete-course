# scope: the region that a variable is recognized
# a variable is only available from inside the region it is created
# a global and locally scoped versions of a variable can be created

def display_name():
    name = "Code"  # local scope (available only inside this function)
    print(name)

# NameError: name 'name' is not defined
# print(name)

name = "Manh Do"  # glocal scope (aveilable inside & outside functions)
print(name)

# LEGB
# local
# enclosing
# global
# built-in