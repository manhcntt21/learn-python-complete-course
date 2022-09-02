# automatic close files
# does not catch and handle any exceptions
try:
    with open("./data/new-file.tx") as file:
        print(file.read())
    print(file.closed)
except FileNotFoundError as e:
    print("That file was not found :(")
except Exception as e:
    print("something went wrong!")
