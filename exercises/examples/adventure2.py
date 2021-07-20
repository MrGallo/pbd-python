current_room = 1

while current_room != 0:
    if current_room == 1:
        # description
        print("Room 1")

        # display options
        print()
        print("[2] Go to room 2")
        print("[3] Go to room 3")
        
        # get choice
        print()
        choice = input("> ")

        # handle choice
        if choice == "2":
            current_room = 2
        elif choice == "3":
            current_room = 3
        else:
            print("Invalid choice.\n")
    elif current_room == 2:
        print("Room 2")
        print("[1] Go back to room 1")

        choice = input("> ")

        if choice == "1":
            current_room = 1
        else:
            print("Invalid choice.")

print("\nEND.")