import os
# move file or folder

# source = "./data/move1"
# destination = "./data/move2/move1"
source = "./data/move1/move1.txt"
destination = "./data/move2/move1.txt"

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print("{} was removed".format(source))
except FileNotFoundError as e:
    print(e)
    print("That {} was not found".format(source))
