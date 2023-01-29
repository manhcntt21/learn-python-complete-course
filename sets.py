# set: collection which is unordered, unindexed. No duplicate values
# a set faster than a list
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

for x in utensils:
    print(x)

utensils = {"fork", "spoon", "knife", "knife", "knife"}
# no duplicate value, three knife but only one knife appears
print(utensils)

# add element
utensils.add("napkin")
print(utensils)

# remove
utensils.remove("fork")
print(utensils)

# clear
utensils.clear()

utensils = {"fork", "spoon", "knife"}

# add one set to another set
utensils.update(dishes)
# dishes.update(utensils # same result)
print(utensils)

# join two set and create a new set
dinner_table = utensils.union(dishes)
print(dinner_table)

utensils = {"fork", "spoon", "knife"}

# compare two set
# utensils have that dishes don't
print(utensils.difference(dishes))
# dishes have that utensils don't
print(dishes.difference(utensils))

# find element of two or more set
print(utensils.intersection(dishes))

# TypeError: 'set' object is not subscriptable
# print(utensils[0])