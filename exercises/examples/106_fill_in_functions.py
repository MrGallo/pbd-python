# Fill-In Functions - Fix the broken functions and function calls.
import random


def main():
    # Fill in the function calls where appropriate.

    print("Watch as we demonstrate functions.")

    print()
    print("I'm going to get a random character from A-Z")
    c = '!'
    # randchar()
    print("The character is: " + c )

    print()
    print("Now let's count from -10 to 10")
    begin = -10
    end = 10
    # counter()
    print("How was that?")

    print()
    print("Now we take the absolute value of a number.")
    y = 99
    x = -10
    # abso()
    print(f"|{x}| = {y}")

    print()
    print("That's all.  This program has been brought to you by:")
    # credits()
}

"""
def credits( ???? ) -> ????:
    # No parameters.
    # displays some boilerplate text saying who wrote this program, etc.

    print()
    print("programmed by Graham Mitchell")
    print("modified by [your name here]")
    print("This code is distributed under the terms of the standard ", end="")
    print("BSD license.  Do with it as you wish.")

    return ??
"""


"""
def randchar( ???? ) -> ????:
    # No parameters.
    # chooses a random character in the range "A" to "Z"
    
    # pick a random number from 0 to 25
    numval = random.randrange(25)
    # now add that offset to the ordinal (ASCII) value of the letter 'A'
    charval = chr(ord('A') + numval)

    return ??
"""


"""
def counter( ???? ) -> ????:
	# Parameters are:
	#     int start
	#     int stop

    # counts from start to stop by ones
    count = start
    while count <= stop:
        print(f"{count} ", end="")
        count += 1

    return ??

"""


"""
def abso( ???? ) -> ????:
    # Parameters are:
    #     int value

    # finds the absolute value of the parameter

    if value < 0:
        absval = -value
    else:
        absval = value

    return ??

"""

if __name__ == "__main__":
    main()