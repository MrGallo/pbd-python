import random
from typing import List


def main():
    # generate random my_listay
    my_list = [random.randrange(100) for _ in range(10)]

    # Display the original (unsorted values)
    print("before: ", end="")
    for n in my_list:
        print(f"{n} ", end="")
    print()

    # sort
    selection_sort(my_list)

    # Display the values again, now after ONE PASS of the exchange sort algorithm.
    print("after : ", end="")
    for n in my_list:
        print(f"{n} ", end="")
    print()


def selection_sort(numbers: List[int]) -> None:
    """Sort a list using the selection sort algorithm.
    
    Args:
        numbers: the list to sort.
    """
    pass


def swap(some_list: List[int], a: int, b: int) -> None:
    """Swaps elements of a list given two index locations.
    
    Args:
        some_list: A list.
        a: First index location
        b: Second index location
    """
    pass


if __name__ == "__main__":
    main()