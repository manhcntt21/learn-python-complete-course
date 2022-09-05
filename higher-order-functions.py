# Higher Order Function: a function either:
#                       1. accepts a functions as an argument
#                       OR         * OR *       OR
#                       2. returns a function
#                       (In python, functions are also treated as object)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func('Hello')
    print(text)
# -------------------------------------------------------------------------------------------
# divisor is a higer order function (a function return a function)
def divisor(x):
    def dividend(y):
        return y/x
    return dividend


if __name__ == '__main__':
    hello(loud)
    hello(quiet)

    divide = divisor(10)
    print(divide)
    print(divide(5))
