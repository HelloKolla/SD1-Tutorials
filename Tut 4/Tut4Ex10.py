# Import required packages

import random

#function for checking if user input is an integer

def is_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

hidden = random.randint(1, 20)                  # Initialize variable 'hidden' with random value
is_valid_input = False                           # Var that is used for is_int function
intGuess = 0
attempts = 5
attemptsForWin = 0
highOrLow = ""

while attempts > 0:
    userGuess = input("Enter your guess for what the number may be! : ")
    is_valid_input = is_int(userGuess)
    while not is_valid_input:
        print("Oh dear, it seems your guess is not a number! Try again!")
        userGuess = input("Enter your guess for what the number may be! : ")
        is_valid_input = is_int(userGuess)
    intUserGuess = int(userGuess)
    if intUserGuess == hidden:
        attempts = -1
        attemptsForWin += 1
        print(f"Good job, you figured it out, in just {attemptsForWin} guesses! The answer is {hidden}!")
    else:
        if intUserGuess > hidden:
            highOrLow = "higher"
        else:
            highOrLow = "lower"
        attempts = attempts - 1
        attemptsForWin += 1
        if attempts > 0:
            print(f"Nice try, but you are wrong! Your guess has a {highOrLow} value compared to the answer. You have {attempts} attempts left!")

if attempts == 0:
    print("You're out of chances! You lose!")
exit()