# Finding Prime Numbers

In a file called `finding_primes.py` ...

Write a function like so:

```python
def is_prime(n: int) -> bool:
    """Determine whether or not a number is prime.

    Args:
        n: the number to check
    
    Returns:
        True if the number is prime, False otherwise.

    """
```

Remember that a number is prime if is isn't evenly divisible by *anything* except for `1` and itself. You can figure this out by using a `for` loop inside the `is_prime` function.


Make the `f` loop run through all the numbers from `2` up to `n`. Inside the loop, use an `if` statement that determines if `n` is evenly divisible by your loop counter variable.

If you find *any* number which divides it evenly, you can go ahead and return `False` from the function without finishing the loop.


If the loop finishes and doesn't find any numbers which divide it, then return `True` from the function.


After you finish writing the function write a `main()` function that contains another `for` loop. Have it print out all the numbers from `2` to `20`, and mark each prime number with a `"<"`.

```
2 <
3 <
4
5 <
6
7 <
8
9
10
11 <
12
13 <
14
15
16
17 <
18
19 <
20

```

If you prefer, you may print out *only* the prime numbers
up to `100` or so, like this:

```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)