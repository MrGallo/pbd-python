# Function Call Alphabet - Yet another program to practice functions, but this time it's function calls only.


def main():
    # ???? a(????)    # displays a word beginning with A
    # ???? b(????)    # returns the word to be displayed
    # ???? c(????)    # pass it True and it will display a word beginning with C
    # ???? d(????)    # displays a word beginning with D
    # ???? e(????)    # pass it the number of letters to display (9)
    # ???? f(????)    # displays the word you pass it beginning with "F"
    # ???? g(????)    # returns the word to be displayed
    # ???? h(????)    # tell it how many times to display the word (1)
    print()

    # ???? i(????)    # pass it any integer and it will display a word beginning with I 
    # ???? j(????)    # returns a different word depending on what you pass it (1-3)
    # ???? k(????)    # displays a word beginning with K
    # ???? l(????)    # displays a different word depending on the two booleans you pass it
    # ???? m(????)    # displays a different word depending on the two booleans you pass it
    # ???? n(????)    # displays the word you pass it beginning with "N"
    # ???? o(????)    # displays a word beginning with O and returns a useless value
    # ???? p(????)    # returns the word to be displayed
    # ???? q(????)    # displays the word
    print()

    # ???? r(????)    # returns a different word depending on if you pass it True or False
    # ???? s(????)    # pass it the number of letters to display (6)
    # ???? t(????)    # displays the word you pass it beginning with "T"
    # ???? u(????)    # returns the word to be displayed
    # ???? v(????)    # tell it how many times to display the word (1)
    # ???? w(????)    # pass it any integer and it will display a word beginning with W 
    # ???? x(????)    # returns a different word depending on what you pass it (1-2)
    # ???? y(????)    # displays a word beginning with Y
    # ???? z(????)    # returns a different word depending on which two boolean values you pass it
    print()

"""
/**************************************
* Don't change anything below here!! *
*************************************/
"""

def a() -> None:
    print("Ant ", end="")


def b() -> str:
    return "Banana "


def c(doit: bool) -> None:
    if (doit):
        print("Crocodile ", end="")


def d() -> None:
    print("Doggie ", end="")


def e(howmany: int) -> None:
    s = "Elephant "
    x = 0
    while x < howmany:
        print(s[x], end="")
        x = x + 1
    

def f(word: str) -> None:
    print(word + " ", end="")


def g() -> str:
    return "Gorilla "


def h(reps: int)  -> None:
    x = 0
    while x < reps:
        print("Horseradish ", end="")
        x = x + 1


def i(ignoredparameter: int) -> None:
    ignoredparameter = 32
    space = chr(ignoredparameter)
    print("Ice_cream" + space, end="")


def j(whichone: int) -> str:
    if whichone == 1:
        return "Jambalaya "
    elif whichone == 2:
        return "Juniper "
    else:
        return "Jackrabbit "


def k() -> None:
    # the bird OR the fruit
    print("Kiwi ", end="")


def l(a: bool, b: bool) -> None:
    if a and b:
        print("Lettuce ", end="")
    else:
        print("Lhasa_apso ", end="")


def m(a: bool, b: bool) -> None:
    if a is True or b is True:
        print("Mango ", end="")
    else:
        print("Monkey! ", end="")


def n(word: str) -> None:
    print(word + " ", end="")


def o() -> int:
    print("Orangutan ", end="")
    return 1	# just for kicks the return value doesn't mean anything


def p() -> str:
    return "Parrot "


def q() -> None:
    print("Quail ", end="")


def r(first: bool) -> str:
    if first is true:
        return "Rabbit "
    else:
        return "Radish "


def s(howmany: int) -> None:
    s = "Snake "
    x = 0
    while x < howmany:
        print(s[x], end="")
        x = x + 1

def t(word: str) -> None:
    print(word + " ", end="")


def u() -> str:
    return "Ugli_fruit "


def v(reps: int) -> None:
    x = 0
    while x < reps:
        print("Valentine_candy ", end="")
        x = x + 1


def w(ignoredparameter: int) -> None:
    ignoredparameter = 32
    space = chr(ignoredparameter)
    print("Walrus" + space, end="")


def x(whichone: int) -> str:
    if whichone == 1:
        return "X_files "
    else:
        return "X_men "


def y() -> None:
    print("Yams ", end="")


def z(a: bool, b: bool) -> str:
    if a or b:
        return "Zanahorias "
    else:
        return "Zebra "


if __name__ == "__main__":
    main()