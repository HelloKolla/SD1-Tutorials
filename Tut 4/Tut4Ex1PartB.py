
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
main_loop_var = False                            # Var that is used for the main loop
intGuess = 0

while main_loop_var == False:
    userGuess = input("Enter your guess for what the number may be! : ")
    is_valid_input = is_int(userGuess)
    while not is_valid_input:
        print("Oh dear, it seems your guess is not a number! Try again!")
        userGuess = input("Enter your guess for what the number may be! : ")
        is_valid_input = is_int(userGuess)
    intUserGuess = int(userGuess)
    if intUserGuess == hidden:
        print("Good job, you figured it out!")
        main_loop_var = True
    else:
        print("Nice try, but you are wrong! Try again!")
exit()