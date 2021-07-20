# Flip Again?

In this program, you'll see how using a "while True and break" (post-test) loop might be better than a regular `while` loop.


## Files Needed

* [057_flip_again.py](examples/057_flip_again.py)


What You Should See
-------------------

The code I have provided does not run. Once you fix it, it will look roughly like this.

```
You flip a coin and it is... TAILS
Would you like to flip again (y/n)? y
You flip a coin and it is... HEADS
Would you like to flip again (y/n)? y
You flip a coin and it is... HEADS
Would you like to flip again (y/n)? n
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. The code as given does not run. Notice that the `while` tests if `again == "y"`, but the variable `again` doesn't have a string value at first. Give it a string value so that the code will not encounter a run-time error and the loop will run at least once.
2. Now that program is working, change the loop from a *pre-test* `while` loop to a *post-test* "while-true" loop. Make sure it still works. 
3. What happens if you delete the `again = "y"` line right before the loop? Does the program still work? Why or why not? (Answer in a comment.)


---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)