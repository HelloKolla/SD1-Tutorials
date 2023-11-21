total = 0 # sum of scores
count = 0 # number of scores entered

# get one score & convert string to integer
score = int(input("Enter score, (Enter -9 to end): ") )

while not score == -9:                                          # Add while loop here. Loop while score is not -9
    total += score                                              # Add score to total
    count += 1                                                  # Keep a count of scores
    score = int(input("Enter score, (Enter -9 to end): ") )     # Get next score input

if total == 0:
    print("No values were entered. No average was calculated.")
    exit()

# print average of scores entered
average = float( total ) / count
print("Class average is", average)