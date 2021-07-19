# Flip Again?


In this program, you'll see how using a do-while loop
might be better than a `while` loop.


## Files Needed


* [FlipAgain.java](examples/FlipAgain.java)


What You Should See
-------------------


The code I have provided does not compile. Once you fix it,
it will look roughly like this.



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


1. The code as given does not compile. Notice that the `while`
 loop tests if `again.equals("y")`, but the variable `again`
 doesn't have a value at first. Give it a value so that the code will compile and 
 the loop will run at least once.

 - Now that program is working, change the loop from a `while`
 loop to a do-while loop. Make sure it still works.

 - What happens if you delete what you added in step 1? Change the line back
 to just `String again;` Does the program still work? Why or why not?
 (Answer in a comment.)





```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)