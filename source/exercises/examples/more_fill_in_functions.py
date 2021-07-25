# More Fill-In Functions - Fix the broken functions and function calls (again).
import random


def main():
    # Fill in the function calls where indicated.
    print("Here we go.")

    print()
    print("Some random numbers, if you please: ")
    low = 1
    high = 10
    val1 =  999  # call superrand() for this value, put low first
    print(f"First: {val1}")
    val2 = 999  # superrand()  but, put high first
    print(f"Second: {val2}")
    if val1 == val2:
        print("Hey!  They were the same!")
    else:
        print("They were not the same.")

    print()
    print("More counting, but this time not by ones: ", end="")
    # count from 2 to 8 by 2s
    # stepcount()
    # count from 10 to 2 by 2s
    # stepcount()

    print()
    print("Let's figure a project grade.")
    a = 4
    b = 3
    c = 4
    d = 5
    e = 2
    f = 1
    result = 999
    # project_grade()
    print(f"434521 -> {result}")

    print()
    print("Finally, some easy ones.", end="")

    nombre = "ERROR"
    # get_name()
    print(f"Hi, {nombre}")

    print()
    print("Do you feel lucky, punk?")
    # crash()
    print()


# def superrand( ???? ) -> ????:
#     """Picks a number between a and b, no matter which is larger.

#     Args:
#         a (int): lower (or higher) bound
#         b (int): higher (or lower) bound
    
#     Returns:
#         The random number between a and b.
#     """
#     if a < b:  # b is larger
#         c = random.randrange(a, b + 1)
#     elif a > b:  # a is larger
#         c = random.randrange(b, a + 1)
#     else:
#         c = a  # or c = b doesn't matter since they're equal

#     return ??


# def stepcount( ???? ) -> ????:
#     """Counts from 'first' to 'last' by 'step'.
    
#     Handles forward and backward.
    
#     Args:
#         first (int):
#         last (int):
#         step (int):
    
#     Returns:
#         None
#     """

#     if first < last:
#         x = first
#         while x <= last:
#             print(f"{x} ", end="")
#             x += step
#     else:
#         x = first
#         while x >= last:
#             print(f"{x} ", end="")
#             x -= step
#     return ??


# def project_grade( ???? ) -> ????:
#     """Get the project's grade.

#     Given six integers representing scores out of five in each of the
#     six categories for the first six weeks project: tells you your
#     overall project grade out of 100

#     Args:
#         p1 (int): first category points.
#         p2 (int): second category points.
#         p3 (int): third category points.
#         p4 (int): fourth category points.
#         p5 (int): fifth category points.
#         p6 (int): sixth category points.
    
#     Returns:
#          (int) the total score
#     """
#     overall_grade = p1 * 6    # six points per point for the first category
#     overall_grade += p2 * 6   # six points per point
#     overall_grade += p3 * 4   # four points per point
#     overall_grade += p4 * 2   # two points per point
#     overall_grade += p5 * 1   # one point per point
#     overall_grade += p6 * 1   # one point per point

#     return ??


# def get_name( ???? ) -> ????:
#     """Finds out the user's name
    
#     Returns:
#         (str) The name
#     """
#     name = input("Please enter your name: ")

#     return ??


# def crash( ???? ) -> ????:
#     """Displays "you win" or "you lose".  You lose 90% of the time.
    
#     Returns:
#         None
#     """
#     if random.randrange(10) == 0:
#         # What do you know?  We won!
#         magic_word = "win"
#     else:
#         # No big suprise we lost.
#         magic_word = "lose"

#     print("you " + magic_word)

#     return ??


if __name__ == "__main__":
    main()