# *args: parameter that will pack all argument into a TUPLE
# useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 10
    for i in stuff:
        sum+= i
    return sum

print(add(1,2,3,4,5,6))