# list comprehensions: a way to create a new list with less syntax
# can mimic certain lambda function, easier to read

# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]
# list = [expression (if/else) for item in iterable]


# when not use
squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

# improvement
squares_lp = [i * i for i in range(1, 11)]
print(squares_lp)

# ----------------------------------------------------------------------
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
pass_student_filter = list(filter(lambda x: x >= 60, students))
print(pass_student_filter)

# improvement
pass_student_lp = [i for i in students if i >= 60]
print(pass_student_lp)

pass_student_lp_2 = [i if i >= 60 else "FALSED" for i in students]
print(pass_student_lp_2)
# ----------------------------------------------------------------------
