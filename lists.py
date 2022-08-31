# lists: used to store multiple items in a single variable

food = ["pizza", "hamburger", "hot-dog", "spaghetti"]
print(food)

# access element in a list
print(food[0])
print(food[1])
print(food[2])
print(food[3])
# IndexError: list index out of range
# print(food[4])

# change value of element anywhere you want
food[0] = "pudding"
print(food)

# loops with list
for x in food:
    print(x)

# add a element into last
food.append("ice cream")
print(food)

# remove a element
food.remove("ice cream")
print(food)

# remove last element
# food.pop()

# food.insert(0, "cake")

# sort
food.sort()
print(food)

# remove all elements
food.clear()
print(food)