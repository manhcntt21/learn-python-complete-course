# variable is a container for a value.
# Behaves as the value that it contains

# string (str)
# number: (int, float)
# boolean (bool)

#------------------------------------------------------------------
first_name = "Manh"
last_name = "Do"

# combine variable
full_name = first_name + " " + last_name
print("Hello " + full_name)

# Check type of variable
# print(type(full_name))
# class 'str' - short for string
#------------------------------------------------------------------

# int datatype
age = 25
age += + 1
# convert int to string - typecasting
print("Your age is " + str(age))
# print(type(age))

# float datatype
height = 170.5
print("Your height is " + str(height) + "cm")
# print(type(height))

# boolean datatype
# true or false
# good use for if statement
human = True
print("Are you a human: " + str(human))
# print(type(human))

# age = "25"
# age += 1
# print(age)
# TypeError: can only concatenate str (not "int") to str
#------------------------------------------------------------------