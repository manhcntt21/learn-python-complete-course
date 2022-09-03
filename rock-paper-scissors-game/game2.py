# quiz game
# -------------------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print('-------------------------------------------------------')
        print(str(question_number) + ". " + key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    display_score(correct_guesses, guesses)


# -------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1;
    else:
        print("Wrong!")
        return 0


# -------------------------------------------------------
def display_score(correct_guesses, guesses):
    print('-------------------------------------------------------')
    print("RESULT")
    print("Answer:  ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: {}%".format(score))


# -------------------------------------------------------
def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
    "who created Python ": "A",
    "what year was Python created: ": "B",
    "Python is attributed to which comedy group": "C",
    "Is the Earth round: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Mush", "C. Bill Gate", "D. Mark Zuckerbrrg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smash", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth"]
]

if __name__ == '__main__':
    new_game()
    while play_again():
        new_game()
    print("Byeeeeeeeeeeeeeee! See ya")