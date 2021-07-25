# Exchange Sort Inner Loop

Download the following code, and get it to run. Exchange sort works by using a marker at the front of the list and comparing the rest of the list to that marker using a loop. If, as you iterate through the rest of the list, you incounter a number that is smaller than the number at the marker, you need to swap the values.

## Files Needed
```eval_rst
* :download:`exchange_sort_inner.py <examples/exchange_sort_inner.py>`
```

What You Should See
-------------------
```
before: 45 87 39 32 93 86 12 44 75 50
after : 45 87 39 32 93 86 12 44 75 50
```

After you add in the code you're supposed to, you should
see something more like this:

```
before: 45 87 39 32 93 86 12 44 75 50 
after : 12 87 45 39 93 86 32 44 75 50 
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

The exchange sort works by comaring a number at the beginning of the list to the rest of the numbers. If it finds a lower value, it will swap them, putting the smallest at the front. After having looked at every number in the list, the smallest number should be sorted to the front.

1. First make sure you can loop through the *rest* of the values. You have to start your loop at `marker + 1`. Print them out.
2. Add an `if` statement in the loop. When you find a value that is smaller than the value at the marker, print out `"SMALLER"`.
3. What needs to happen next is every time you encounter a smaller value, that smaller value needs to be swapped into the marker slot. 
4. Get rid of the `print` statements inside your exchange sort inner loop and compare your result with the one shown above.

The list won't be completely sorted. This is only one pass. You will need to nest this loop in another loop that will increment your `marker` variable for you. That will be done in the next assignment.

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)