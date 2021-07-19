# Sierpinski Triangle


We're going to use what we've been learning to draw a
famous fractal: the Sierpinski triangle. You'll need to implement
the following steps:


1. Make *certain* that your application specifies
 a WIDTH of 1024 and a HEIGHT of 768 for the Canvas.
 - Create six variables to represent three vertices:
 (512,109), (146,654), and (876,654). I recommend storing
 these as (x1,y1), (x2,y2), and (x3,y3).
 - Create another pair of variables which will store the
 "current" point. You should really call them `x`
 and `y`. Start x at 512, and start y at 382.
 - Then, in a loop that repeats 50,000 times:
	* Draw the current point on the screen
	 by using the following line of code:
	 `g.drawLine(x,y,x,y);`* (optional) Delay for a bit using `Thread.sleep()`* Have the computer choose a random number from 1 to 3
	 * If the random number was a 1, find the distance
	 between (x,y) and (x1,y1)
		+ (You can find the x-distance (which
		 I call `dx`) by subtracting
		 `x - x1`, and you can find
		 `dy` in a similar way.)* If the random number was a 2, find the distance
	 between (x,y) and (x2,y2)
	 * If the random number was a 3, find the distance
	 between (x,y) and (x3,y3)
	 * Move the "current" point half the distance to
	 the chosen vertex like so: `x = x - dx/2;`
	 and (similarly) `y = y - dy/2;`* Again, all of this is in a loop that repeats
	 50,000 times or so.- (optional) Once the loop ends, draw the string
 `"Sierpinski Triangle"` at (462,484) or so.






Here is a working example version:

 Sierpinski


For those who want to know where the random points above come from:


* x1 is half the width of the screen (512)
 * y1 is 1/7 the height of the screen (109)
 * x2 is 1/7 the width of the screen (146)
 * y2 is 6/7 the height of the screen (654)
 * x3 is 6/7 the width of the screen (876)
 * y3 is 6/7 the height of the screen (again, 654)







There's nothing particularly special about these points, but they
form the vertices of a nice-looking equilateral triangle that pretty
much fills the screen. But the fractal would still come out pretty
much no matter which starting values you use for the vertices.


The starting (x,y) could actually be *any* point inside
the triangle. I chose (512,382) because it's smack-dab in the
middle of the triangle and usually gets overwritten by the others.
If you move it somewhere else, the output will still turn out
almost identically.


The Sierpinski triangle is named after Waclaw Sierpinski, who
described it in 1915.



```



```



---


©2013–2015 Graham Mitchell


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)




