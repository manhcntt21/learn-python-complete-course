# walrus operator:     :=

# new to python 3.8
# assignment expression aka (also known as) walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)
# print(happy := True)
# -------------------------------------------------------
# foods = list()
# while True:
#     food = input("what food do you like?: ")
#     if food == 'quit':
#         break
#     foods.append(food)

# same program but use walrus operator
foods = list()
while food := input("what food do you like?: ") != 'quit':
    foods.append(food)