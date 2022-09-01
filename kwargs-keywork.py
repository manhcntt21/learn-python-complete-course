# **kwargs: parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("hello", end=" ")
    for k, v in kwargs.items():
        print(v, end=" ")

hello(title="Mr", first="Manh", middle="Truong", last="Do")
