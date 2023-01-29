class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

xf = x.f

print(xf())
print(x.f())
# x.f() equiavalent to MyClass.f(x)

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

print(C.f(C,1,2))