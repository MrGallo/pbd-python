"""
Room list
1 - Small room
2 - Closet
3 - Hall
4 - Wall
"""

current_room = 1
choice = ""

while current_room != 0:
    if current_room == 1:
        # description
        print("You are in a small room. There is a \"closet\" and a doorway to the \"hall\".")
        
        # get choice
        print()
        choice = input("> ")

        # handle choice
        if choice == "closet":
            current_room = 2
        elif choice == "hall":
            current_room = 3
        else:
            print(choice + " wasn't one of the options. Try again.")

    elif current_room == 2:
        print("You're in a barren closet. There's nothing to do here except go \"back\".")

        choice = input("> ")

        if choice == "back":
            current_room = 1
        else:
            print(choice + " wasn't one of the options. Try again.")
    
    elif current_room == 3:
        print("You find yourself in a concrete hallway. Oddly, there is only a single")
        print("\"door\" visible. Otherwise, the hall just extends about fifteen feet")
        print("in either direction, and ends in a smooth, blank, concrete wall.")
        print("Do you want to enter the \"door\" or approach the \"wall\" looking for clues?")

        choice = input("> ")

        if choice == "door":
            current_room = 1
        elif choice == "wall":
            current_room = 4
        else:
            print(choice + " wasn't one of the options. Try again.")
    
    elif current_room == 4:
        print("Upon closer inspection, the seemingly blank wall shimmers ever so slightly")
        print("in the dim light. You put forward a tentative hand, and it pushes through,")
        print("a feeling of static sliding up your arm.")
        print()
        print("You pass through the portal into the unknown....")
        current_room = 0


print("\nThe game is over. The next episode can be downloaded for only 800 Microsoft points!")
