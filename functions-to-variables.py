def hello():
    print("hello!")


print(hello)  # memory address of where this function is located within my computer
hello()

hi = hello
print(hi)

hi()
hello()
# ----------------------------------------------------------------------------------
say = print
say("Whoa!  I can't believe this works! :0")
