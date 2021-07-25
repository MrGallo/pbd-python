# Heron's Formula


In this program, you'll look at a function that "returns a
value". When you call on the function to do a task, it will
give you back a result.


## Files Needed

```eval_rst
* :download:`herons_formula.py <examples/herons_formula.py>`
```
```eval_rst
* :download:`herons_formula_no_function.py <examples/herons_formula_no_function.py>`
```

Save or rename `herons_formula.py` to `herons_formula.py`

What You Should See
-------------------
```
A triangle with sides 3,3,3 has an area of 2.0
A triangle with sides 3,4,5 has an area of 6.0
A triangle with sides 7,8,9 has an area of 26.832815729997478
A triangle with sides 5,12,13 has an area of 30.0
A triangle with sides 10,9,11 has an area of 42.42640687119285
A triangle with sides 8,15,17 has an area of 60.0

```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. Run both files (`herons_formula.py` and `herons_formula_no_function.py`). Do they both produce the same output? (Answer in a comment in `herons_formula.py`.)
2. How many lines long is `herons_formula_no_function.py`?
 How many lines long is `herons_formula.py` if you don't count the `10` lines of comments inside the `triangle_area()` function? 
 (Put the answers to both questions in a comment in `herons_formula.py`.)
3. There is a bug in the formula for both files. When `(a+b+c)` is an odd
 number, floor-dividing by `2` throws away the `.5`. Fix **both** files
 so that instead of `(a+b+c) // 2` you have `(a+b+c) / 2` everywhere
 it occurs. Was it easier to fix the file that used a function, or the one that didn't use a function? Answer in a comment.
4. Add one more test to **both** files: find the area of a triangle with sides `9`, `9`, and `9`. Was it difficult to add to the file that used a function? Answer in a comment on the line below where you added the new function call.
5. (You don't need to turn in `herons_formula_no_function.py`. Only turn in one file: `herons_formula.py`)

What You Should See After Everything Is Done
--------------------------------------------

```
A triangle with sides 3,3,3 has an area of 3.897114317029974
A triangle with sides 3,4,5 has an area of 6.0
A triangle with sides 7,8,9 has an area of 26.832815729997478
A triangle with sides 5,12,13 has an area of 30.0
A triangle with sides 10,9,11 has an area of 42.42640687119285
A triangle with sides 8,15,17 has an area of 60.0
A triangle with sides 9,9,9 has an area of 35.074028853269766

```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)