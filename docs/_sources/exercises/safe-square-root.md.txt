# Safe Square Root

Write a program to take the square root of a number typed in by
the user. Your program should use a loop to ensure that the number they
typed in is positive. If the number is negative, you should print out
some sort of warning and make them type it in again.

You can get the square root of a number `n` with
`math.sqrt(n)`, if you import the `math` library.

```python
import math


math.sqrt(49)  # 7
```

Make sure you don't try to find the square root until the loop is done and you know *for sure* you've got a positive number.

Name the file: `safe_square_root.py`

```
SQUARE ROOT!
Enter a number: 9
The square root of 9 is 3.0.

```

```
SQUARE ROOT!
Enter a number: 2
The square root of 2 is 1.4142135623730951.

```

```
SQUARE ROOT!
Enter a number: -9
You can't take the square root of a negative number, silly.
Try again: -10
You can't take the square root of a negative number, silly.
Try again: 10
The square root of 10 is 3.1622776601683795.

```

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)