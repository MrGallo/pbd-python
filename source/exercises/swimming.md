# Swimming


So far you have only worked with one type of loop: the `while`
loop. But there is another type: the "do-while" loop.


The do-while loop works *almost* exactly like a
`while` loop. In fact, most of the time they
are equivalent. Examine the program below to see if you can figure
out the tiny difference.


## Files Needed

* [swimming.py](../_static/examples/swimming.py)


What You Should See
-------------------

Goofus and Gallant are both going swimming. They hate to swim in cold water; once the water temperature drops below `79°`F, they stop.


Run the program, and type in `80.5` for the water temperature.

```
What is the current water temperature? 80.5

Okay, so the current water temperature is 80.5 F.
GALLANT approaches the lake....
    GALLANT swims for a bit. Swim time: 1 min.
    The current water temperature is now 80.0 F.
    GALLANT swims for a bit. Swim time: 2 min.
    The current water temperature is now 79.5 F.
    GALLANT swims for a bit. Swim time: 3 min.
    The current water temperature is now 79.0 F.
    GALLANT swims for a bit. Swim time: 4 min.
    The current water temperature is now 78.5 F.
GALLANT stops swimming. Total swim time: 4 min.

Okay, so the current water temperature is 80.5 F.
GOOFUS  approaches the lake....
    GOOFUS  swims for a bit. Swim time: 1 min.
    The current water temperature is now 80.0 F.
    GOOFUS  swims for a bit. Swim time: 2 min.
    The current water temperature is now 79.5 F.
    GOOFUS  swims for a bit. Swim time: 3 min.
    The current water temperature is now 79.0 F.
    GOOFUS  swims for a bit. Swim time: 4 min.
    The current water temperature is now 78.5 F.
GOOFUS  stops swimming. Total swim time: 4 min.

```

What You Should Do on Your Own
------------------------------

Assignments turned in *without* these things will receive
no credit.

1. Run the program, and type in 80.5 for the current
 water temperature. Do Goofus and Gallant swim for the same amount of
 time? Put your answer in a comment.
2. Run the program again, but this time enter 78 for the starting temperature. What changes?
3. Does Gallant check the water temperature first, or does he just dive right in?
4. What about Goofus? Does he check the water temperature first or just dive in?
5. What is the difference between the first `while` loop and the second `while` loop? What do you suppose the keyword `break` does in the second loop?
6. One of these loops is sometimes called a "pre-test loop",
 and the other is called a "post-test loop". Which one is which?

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)