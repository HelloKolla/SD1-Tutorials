loop1 = 0

while loop1 == 0:
    try:
        option = int(input("Select a menu (1, 2, 3, or 4 to quit): "))
        if option == 1:
            print("1 selected")
        elif option == 2:
            print("2 selected")
        elif option == 3:
            print("3 selected")
        elif option == 4:
            print("Quit selected")
            break
        else:
            print("Option not recognized")
    except ValueError:
        print("Enter an integer")