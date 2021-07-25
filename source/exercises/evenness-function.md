# Evenness Function

In a file called `evenness_function.py` ...

Write a function like so:

```python
def is_even(n: int) -> bool:
    """Determine if a number is even.

    Args:
        n: the number to check
    
    Returns:
        True if the number is even, False otherwise.
    """
```

Also write:

```python
def is_divisible_by_3(n: int) -> bool:
    """Determines if a number is evenly divisible by 3.

    Args:
        n: The number to check
    
    Returns:
        True if the number is divisible by 3. False otherwise.
    """
```
Write a `main()` funciton that contains a `for` loop to generate all the numbers from `1` to `20`. Use `if` statements inside the loop to mark the number with a `"<"` if it's even, with a `"="` if it's evenly divisible by `3`, and with both if it's divisible by both `2` and `3`.

```
1
2 <
3 =
4 <
5
6 <
6 =
7
8 <
9 =
10 <
11
12 <
12 =
13
14 <
15 =
16 <
17
18 <
18 =
19
20 <
```

If you're cool, it's possible to make the display like this:
```
1
2 <
3 =
4 <
5
6 <=
7
8 <
9 =
10 <
11
12 <=
13
14 <
15 =
16 <
17
18 <=
19
20 <

```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)