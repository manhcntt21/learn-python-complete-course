# exception: events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:  # handle a specific exception
    print(e)
    print("you cann't divide by zero! idiot!")
except ValueError as e:  # handle a specific exception
    print(e)
    print("enter only number, pls")
except Exception as e:  # handle all exception
    print(e)
    print("something went wrong! :(")
else:
    print(result)
finally:  # always execute
    # open file and close file
    print("This will always execute!")