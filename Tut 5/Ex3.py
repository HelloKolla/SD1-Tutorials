# Ask the user for their username
username = input("Enter a username of 6 characters: ")

# Check if the username is 6 characters long
if len(username) == 6:
    print("Username is valid.")
else:
    print("Username must be 6 characters long.")
