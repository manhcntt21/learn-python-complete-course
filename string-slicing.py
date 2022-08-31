# slicing: create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

# ------------------------------------------------------------
# indexing
name = "Manh Do"
first_name = name[:4]
last_name = name[5:]
funky_name = name[::3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
# ------------------------------------------------------------
# slicing
website = "https://google.com"
website2 = "https://wikipedia.com"

# slice object
name_website = slice(8, -4, )

print(website[name_website])
print(website2[name_website])