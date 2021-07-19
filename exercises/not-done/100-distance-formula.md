# Distance Formula


Write a function to compute the distance between two points. Given
two points (*x*1,
*y*1) and (*x*2, *y*2),
the distance between these points is given by the formula:




|  |
| --- |
| ![the distance formula](examples/distance_formula.gif) |


You must name the function `distance`, and it must return a 
`double` giving the distance between the two points.


## Files Needed


* [DistanceFormula.java](examples/DistanceFormula.java)



```
 
public class DistanceFormula
{
	public static void main( String[] args )
	{
		// test the formula a bit
		double d1 = distance(-2,1 , 1,5);
		System.out.println(" (-2,1) to (1,5) => " + d1 );
 
		double d2 = distance(-2,-3 , -4,4);
		System.out.println(" (-2,-3) to (-4,4) => " + d2 );
 
		System.out.println(" (2,-3) to (-1,-2) => " + distance(2,-3,-1,-2) );
 
		System.out.println(" (4,5) to (4,5) => " + distance(4,5,4,5) );
	}
 
	public static double distance( int x1, int y1, int x2, int y2 )
	{
		// put your code up in here
	}
}

```


```
 
 (-2,1) to (1,5) => 5.0
 (-2,-3) to (-4,4) => 7.280109889280518
 (2,-3) to (-1,-2) => 3.1622776601683795
 (4,5) to (4,5) => 0.0

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)