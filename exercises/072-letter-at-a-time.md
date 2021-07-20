# Letter at a Time


Did you know that using a for loop, you can examine a string one letter at a time? You can use `range` and tell it how long the string is.


* `len()` returns an `int`
 representing the total number of characters in the String
 (including punctuation and whitespace). For example, if
 the variable `str` contains the String `"hello"`, then `len(str)` will
 return `5`.

 * `[n]` returns the
 `n`th character (`char`)
 in the String. The character positions are zero-based. If the variable `str` contains the String `"ligature"`, then `str[0]` (`str` at index `0`) will return `'l'`, and `str[4]` (`str` at index `4`) will return `'t'`.


## Files Needed
* [letter_at_a_time.py](examples/letter_at_a_time.py)

Save the file as: `072_letter_at_a_time.py`

What You Should See
-------------------
```
What is your message? Are you ready for this?

Your message is 23 characters long.
The first character is at index 0 and is 'A'.
The last character is at index 22 and is '?'.

Here are all the characters, one at a time:

    0 - 'A'
    1 - 'r'
    2 - 'e'
    3 - ' '
    4 - 'y'
    5 - 'o'
    6 - 'u'
    7 - ' '
    8 - 'r'
    9 - 'e'
    10 - 'a'
    11 - 'd'
    12 - 'y'
    13 - ' '
    14 - 'f'
    15 - 'o'
    16 - 'r'
    17 - ' '
    18 - 't'
    19 - 'h'
    20 - 'i'
    21 - 's'
    22 - '?'

Your message contains the letter 'a' 2 times.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
half credit or less.

1. If you print `range(7)`, what do you see? What happens if you convert the range to a list and then print that out? E.g., `list(range(7))`
2. The `for` loop is defined so that the loop variable `i` iterates through the entire range object `range(len(message))`. If the `message` was `"Hello"` what number would be sent to the range function? What numbers would be included within that range object? List them out.
3. If a string variable contains the value `"box"`, what is its length? What is the index (position) of the last character (the `'x'`)?
4. Currently the code prints out the number of 'a's in the message. Change it so that it instead prints out the number of vowels (`a A e E i I o O u U`).

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)