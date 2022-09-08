# if __name__ == '__main__':

# python interpreter sets 'special variables', one of which is __name__
# python will assign the __name__ variable a value of '__main__' if, it's the initial module beeing run
import messages

print(__name__)
print(messages.__name__)

if __name__ == '__main__':
    print('running this module directly')
else:
    print('running other module directly')