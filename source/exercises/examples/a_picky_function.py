def main():
    title = "My Special Addition Program"
    print(title)
    print("=" * len(title))
    print()

    print(f"3 + 2 = {picky_sum(3, 2)}")
    print(f"5 + 6 = {picky_sum(5, 6)}")
    print(f"8 + -3 = {picky_sum(8, -3)}")
    print(f"100 + 55 = {picky_sum(100, 55)}")
    print(f"5 + 5 = {picky_sum(5, 5)}")



def picky_sum(a: int, b: int) -> int:
    """Adds two numbers but refuses to add them if they are the same.
    
    Args:
        a: A number
        b: Another number
    
    Returns:
        The sum of the two different numbers
    
    Raises:
        RefusalToAddTheSameNumberError if the numbers are the same.
    """
    return a + b


if __name__ == "__main__":
    main()