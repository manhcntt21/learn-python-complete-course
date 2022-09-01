# tuple: collection which is ordered and unchangeable
# used to group together related data

student = ("Manh Do", 25, "male")

# tuple functions
print(student.count("Manh Do"))
print(student.index("male"))

# iteration in tuple
for x in student:
    print(x)

# check value exist
if "Manh Do" in student:
    print("Manh Do is here!")