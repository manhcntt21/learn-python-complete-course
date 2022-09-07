# sort() method:    used with lists
# sort() function:  used with iterables

# name, grade, age
student = (
    ('Michael', 'F', 60),
    ('Lincoln', 'A', 33),
    ('T-Bag', 'B', 36),
    ('Secure', 'C', 20)
)
student_list = ['Michael', 'Lincoln', 'T-Bag', 'Secure']
# -------------------------------------------------------------
print('before: {}'.format(student_list))
student_list.sort(reverse=False)  # reverse = False meaning descending, in contrast meaning ascending
print('after: {}'.format(student_list))
grade = lambda grades: grades[1]  # iterable
# reverse = False meaning descending, in contrast meaning ascending
sorted_student = sorted(student, reverse=False, key=grade)  # function object

print(sorted_student)
