

def main():
    print("Welcome to Mr. Gallo's fantastic birth-o-meter!")
    print()
    print("All you have to do is enter your birthday, and it will tell you")
    print("the day of the week on which you were born.")
    print()
    print("Some automatic tests....")
    print(f"12 10 2003 => {weekday(12, 10, 2003)}")  # Wednesday, December 10, 2003
    print(f"2 13 1976 => {weekday(2, 13, 1976)}")  # Friday, February 13, 1976
    print(f"2 13 1977 => {weekday(2, 13, 1977)}")  # Sunday, February 13, 1977
    print(f"7 2 1974 => {weekday(7, 2, 1974)}")  # Tuesday, July 2, 1974
    print(f"1 15 2003 => {weekday(1, 15, 2003)}")  # Wednesday, January 15, 2003
    print(f"10 13 2000 => {weekday(10, 13, 2000)}")  # Friday, October 13, 2000

    print("Now it's your turn!  What's your birthday?")
    print("Birth date (mm dd yyyy): ")
    mm = int(input("mm: "))
    dd = int(input("dd: "))
    yyyy = int(input("yyyy: "))
    
    # put a function call for weekday() here
    print("\nYou were born on ")



def weekday(mm: int, dd: int, yyyy: int) -> str:
    years_since_1900 = 0  # step 1
    total = 0  # step 2

    # steps 3-7 go here

    date_string = f"{month_name(mm)}, {yyyy}"  # step 8

    return date_string


# paste your functions from month_name, weekday_name, and month_offset here


def is_leap(year: int) -> bool:
    # years which are evenly divisible by 4 are leap years,
    # but years divisible by 100 are not leap years,
    # though years divisible by 400 are leap years

    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    
    return result


if __name__ == "__main__":
    main()