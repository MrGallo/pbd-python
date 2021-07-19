# Month Name



Write a function. It will return the name of a month of the year,
given the month number, according to the table below. Make sure you
**do not** put any input or output statements in the function;
the month number will be *passed in* and the string containing
the name will be *returned*.




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number Month
| 1 January
| 2 February
| 3 March
| 4 April
| 5 May
| 6 June
| 7 July
| 8 August
| 9 September
| 10 October
| 11 November
| 12 December
| anything else error
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |
 | |




The function **must** be called `month_name()`,
and must have one parameter (an integer), and return a
`String`.


And finally, here's some starter code.


* [MonthName.java](examples/MonthName.java)



```
public static void main( String[] args )

    System.out.println( "Month 1: " + month\_name(1) );
    System.out.println( "Month 2: " + month\_name(2) );
    System.out.println( "Month 3: " + month\_name(3) );
    System.out.println( "Month 4: " + month\_name(4) );
    System.out.println( "Month 5: " + month\_name(5) );
    System.out.println( "Month 6: " + month\_name(6) );
    System.out.println( "Month 7: " + month\_name(7) );
    System.out.println( "Month 8: " + month\_name(8) );
    System.out.println( "Month 9: " + month\_name(9) );
    System.out.println( "Month 10: " + month\_name(10) );
    System.out.println( "Month 11: " + month\_name(11) );
    System.out.println( "Month 12: " + month\_name(12) );
    System.out.println( "Month 43: " + month\_name(43) );
}

```



```
Month 1: January
Month 2: February
Month 3: March
Month 4: April
Month 5: May
Month 6: June
Month 7: July
Month 8: August
Month 9: September
Month 10: October
Month 11: November
Month 12: December
Month 43: error

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)