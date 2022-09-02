import random

x = random.randint(1, 6)
# random number between 0 and 1
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
# shuffle list
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)