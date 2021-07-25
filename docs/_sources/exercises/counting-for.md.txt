# Counting with a For Loop


As you saw in [Counting with a While Loop](counting-while.md),
a `while` loop can be used to to make something happen an
exact number of times.

However, this isn't our best choice. `while` loops are
designed to keep going *as long as* something is true. But if we know
in advance how many times we want to do something, Python has a special kind of loop designed just for that: the `for` loop.

Type in the following code, and get it to run. Then answer the
questions down below.

Name the file: `counting_for.py`


```python
print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(0, 5, 1):
    print(f"{n}. {message}")
```

`for` loops are best when we know in advance how many times we want to do something.


* Do this ten times.
* Do this five times.
* Pick a random number, and do it that many times.
* Take this list of items, and do it one time for each item in the list.

On the other hand, `while` loops are best for repeating *as long as*
something is true:

* Keep going as long as the player's health is greater than `0`.
* Keep going as long as they haven't guessed it.
* Keep going as long as they keep typing in a negative number.
* Keep going as long as they haven't typed in a zero.

What You Should See
-------------------
```
Type in a message, and I'll display it five times.
Message: Hello, Goodbye!
0. Hello, Goodbye!
1. Hello, Goodbye!
2. Hello, Goodbye!
3. Hello, Goodbye!
4. Hello, Goodbye!
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. What happens when you change the loop variable `n` to some other name?(Then change it back.) Why do you suppose I chose to name this particular loop variable "n"?
2. How do the first two arguments (`0, 5`) given to the `range` function effect the loop? Change them and experiment. Change it back.
3. What do you suppose the third number given to the `range` function is for? Change it to `2` and see. Change it back.
4. What happens when you call the `range` function with only one number? i.e. `range(7)`?
5. What happens when you call the range function with only two numbers? i.e. `range(3, 9)`?
6. Change the code so that the loop repeats ten times instead of five.
7. See if you can change the for loop so that the message starts at 2 and counts by twos, like so:
    ```
    Type in a message, and I'll display it ten times.
    Message: qwerty
    2. qwerty
    4. qwerty
    6. qwerty
    8. qwerty
    10. qwerty
    12. qwerty
    14. qwerty
    16. qwerty
    18. qwerty
    20. qwerty
    ```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)