# lambda function: function wrritten in 1 line using lambda keyword
# accepts any number or arguments, but only has one expression
# (think of it as shortcut)
# useful if needed for a short period of time, throw-away

# lambda parameters: expression

# normal function
def double(x):
    return x * 2

print(double(5))
# lambda function
double2 = lambda x: x * 2
multiple = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + ' ' + last_name
age_check = lambda age: True if age >= 18 else False

print(double2(5))
print(multiple(5, 10))
print(add(1, 2, 3))
print(full_name('Michael', 'Do'))
print(age_check(20))