# Project: Calculator


Write a calculator program. A minimal calculator will support
the following functions:

* numbers with decimals (not just integers)
* addition (`1 + 2` is `3`)
* subtraction (`12 - 4` is `8`)
* multiplication (`33 * 2` is `66`)
* division (`3 / 8` is `0.375`)
* exponents (`2 ^ 3` is `8`)
* error messages when you do something wrong


Name your file `115_calculator.py`


Your calculator should keep on running until explicitly told to quit. I suggest typing a zero as the first operand to cause it to quit, i.e.

```
>2 + 3
5
>4 * 9
36
>0 + 2
Bye, now.
```

Programs may support other features if desired. Suggested other
functions to add include:


* modulus (10 % 3 is 1)
* factorials (4 ! is 4*3*2*1, a.k.a. 24)
* trigonometric functions (sin,cos,tan)
* square roots
* negation (- -3 is 3)
* angles in degrees or radians
* a help feature to display legal syntax and supported functions
* previous result used as first operand
* the ability to store and recall results
* rounding
* logarithms
* arbitrary roots
* conversion from base 10 to binary (for integers only)

Some students may wonder how to deal with the first operand possibly being a character or a number. That is, how can your program support phrases like `"2 + 3"` (`float str flost`) *and* `"sin 30"` (`str float`) at the same time? Well, if you read in *everything* as a `str`, then there are some python string methods that may be useful to you.

```python
>>> "56".isdigit()
True
>>> "hello".isdigit()
False
>>> "hello".isalpha()
True
```

Checking float numbers is a bit more tricky. Use this function:
```python
def isfloat(s: str) -> bool:
    """Checks if a string contains exclusively a float number.
    
    Note: if the string contains an integer,
    this function will return False.

    Args:
        s: the string to check
    
    Returns:
        True if the string exclusively contains a float.
        False otherwise.
    """
    try:
        assert s.isdigit() is False
        float(s)
    except (ValueError, AssertionError):
        return False
    else:
        return True
```

---


What to avoid
-------------

Any program which presents me with a screen like the following will
not receive a very good score.

```
Enter the function you wish to perform.
1) addition
2) subtraction
3) multiplication
4) division
5) quit
Your choice:

```
Also, the same fate applies to any program that ever presents me with
the following message:


```
 Would you like to calculate again? (y/n) 
```

For some extra points, re-use as many functions as possible. For example, multiplication is really only addition but done multiple times. 

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)