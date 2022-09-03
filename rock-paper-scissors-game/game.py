# game rock, paper, scissors
import random

choices = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper or scissors?: ').lower()

    # game
    if player == computer:
        print("computer: {:>20}".format(computer))
        print("player:   {:>20}".format(player))
        print("Tie!")
    elif player == 'rock':
        if computer == 'paper':
            print("computer: {:>20}".format(computer))
            print("player:   {:>20}".format(player))
            print("You lose!")
        else:
            print("computer: {:>20}".format(computer))
            print("player:   {:>20}".format(player))
            print("You win!")
    elif player == 'paper':
        if computer == 'rock':
            print("computer: {:>20}".format(computer))
            print("player:   {:>20}".format(player))
            print("You win!")
        else:
            print("computer: {:>20}".format(computer))
            print("player:   {:>20}".format(player))
            print("You lose!")
    elif player == 'scissors':
        if computer == 'rock':
            print("computer: {:>20}".format(computer))
            print("player:   {:>20}".format(player))
            print("You lose!")
        else:
            print("computer: {:>20}".format(computer))
            print("player:   {:>20}".format(player))
            print("You win!")

    play_again = input("play again? (yes/no)").lower()
    if play_again != "yes":
        break

print('Bye! See ya')
