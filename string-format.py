# str.format(): optional method that gives users
# more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
# {} - a placeholder
print("The {} jumped over the {}".format("cow", "moon"))
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  # positional argument
print("The {1} jumped over the {0}".format(item, animal))  # positional argument
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

# add some padding to a string when we display it
name = "Manh Do"
print("Hello,my name is {}".format(name))
print("Hello,my name is {:10}".format(name)) # default left alignment
# add left alignment ":<n"
print("Hello,my name is {:<10}. Nice to meet you".format(name))
# add right alignment ":>n"
print("Hello,my name is {:>10}. Nice to meet you".format(name))  # cursor when we blacked out
# add center alignment ":<n"
print("Hello,my name is {:^10}. Nice to meet you".format(name))


# format number
number = 3.14159

# only take two digits after dot
print("The number pi is {:.2f}".format(number))

number2 = 1000
# add separation comma between units
print("The number pi is {:,}".format(number2))
# convert binary number
print("The number pi is {:b}".format(number2))
# convert octal number
print("The number pi is {:o}".format(number2))
# convert hex number
print("The number pi is {:x}".format(number2))
print("The number pi is {:X}".format(number2))
# scientific notation
print("The number pi is {:e}".format(number2))
print("The number pi is {:E}".format(number2))
