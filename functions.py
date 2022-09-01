# function: a block of code which is executed only when it is called

def hello():
    print("hello!")
    print("have a nice day!")


# parameter/argument
def hello2(name):
    print("hello " + name)
    print("have a nice day!")


def hello3(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("have a nice day!")


if __name__ == '__main__':
    my_name = "Manh Do"
    hello()
    hello2(my_name)
    hello3("Manh", "Do", 25)
