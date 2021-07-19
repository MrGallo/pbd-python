# Heron's Formula


In this program, you'll look at a function that "returns a
value". When you call on the function to do a task, it will
give you back a result.


## Files Needed


* [HeronsFormula.java](examples/HeronsFormula.java)* [HeronsFormulaNoFunction.java](examples/HeronsFormulaNoFunction.java)



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


1. Compile and run both files (HeronsFormula.java and HeronsFormulaNoFunction.java).
 Do they both produce the same output? (Answer in a comment in HeronsFormula.java.)

 - How many lines long is HeronsFormulaNoFunction.java?
 How many lines long is HeronsFormula.java if you don't count the two lines
 of comments inside the `triangleArea()` function? 
 (Put the answers to both questions in a comment in HeronsFormula.java.)

 - There is a bug in the formula for both files. When `(a+b+c)` is an odd
 number, dividing by `2` throws away the `.5`. Fix both files
 so that instead of `(a+b+c) / 2` you have `(a+b+c) / 2.0` everywhere
 it occurs. Was it easier to fix the file that used a function, or the one that didn't
 use a function? Answer in a comment.

 - Add one more test to both files: find the area of a triangle with sides 9, 9, and 9.
 Was it difficult to add to the file that used a function? Answer in a comment on the line
 below where you added the new function call.

 - (You don't need to turn in HeronsFormulaNoFunction.java. Only turn in one file:
 HeronsFormula.java)






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


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)