# Store the secret word in a variable
secret = "water"

# Initialize the number of guesses the player has remaining
guesses_remaining = 6

# Initialize a variable to store the player's guesses
guesses = ""

win = False

print("Welcome to the guessing game!")
print(f"You have {guesses_remaining} guesses remaining.")
print("_ " * len(secret))
# Start the game loop
while guesses_remaining > 0:

    # Ask the player for their guess
    player_guess = input("Guess a letter: ")

    # Convert the player's guess to lowercase
    player_guess = player_guess.lower()

    # Check if the player's guess is in the secret word
    if player_guess in secret:

        # Add the player's guess to the player's guesses variable
        guesses += player_guess

        # Print the updated secret word with the player's guesses revealed
        updated_secret = ""
        for letter in secret:
            if letter in guesses:
                updated_secret += letter
            else:
                updated_secret += "_"
        print(f"Secret word : {updated_secret}")
        guesses_remaining -= 1
        print(f"You have {guesses_remaining} guesses remaining.")

        # Check if the player has guessed the secret word
        if updated_secret == secret:
            print("Congratulations! You guessed the secret word correctly.")
            win = True
            break

    else:

        # Reduce the number of guesses the player has remaining
        guesses_remaining -= 1

        # Print a message to the player letting them know their guess was incorrect
        print(f"Incorrect guess. You have {guesses_remaining} guesses remaining.")

# If the player runs out of guesses, print a message to the player letting them know they lost
if guesses_remaining == 0 & win == False:
    print(f"Sorry, you ran out of guesses. The secret word was \'{secret}\'.")
