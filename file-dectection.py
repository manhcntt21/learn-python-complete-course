import os

path = "D:\\CODE\\learn-python-complete-course\\data\\new-folder"

# check exist
if os.path.exists(path):
    print("That location exists")
    # check a file or not
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")