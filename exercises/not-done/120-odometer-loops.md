# Odometer Loops


Download the following code, and get it to compile.


## Files Needed


* [OdometerLoops.java](examples/OdometerLoops.java)



```
public class OdometerLoops
{
    public static void main( String[] args ) throws Exception
    {
        for ( int thous=0; thous<10; thous++ )
        {
            for ( int hund=0; hund<10; hund++ )
            {
                for ( int tens=0; tens<10; tens++ )
                {
                    for ( int ones=0; ones<10; ones++ )
                    {
                        System.out.print( " " + thous + "" + hund + "" + tens + "" + ones + "\r" );
                        Thread.sleep(10);
                    }
                }
            }
        }

        System.out.println();
    }
}

```

What You Should See
-------------------



```
 9999

```

(It looks a little cooler in person.)

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
no credit.


1. Delete all the open braces and close braces from all the outer
 `for` loops. (Leave the curly braces that belong
 to the innermost loop (the "ones" loop).) Does it still work? Answer
 in a comment.

 - Change all the loops so that they count from 0 to 7 instead of
 0 to 9. This will display numbers in "octal" (base 8) instead of
 "decimal" (base 10).

 - Change the code so that the human gets to type in a number for
 the base, and your odometer counts up to that instead of 8. You might
 want to increase the delay (put a bigger number (like maybe 500) inside
 the `Thread.sleep()`).




After you've made all the changes, it should look something like this
(except that all your numbers will be overwriting each other on the same
line instead of printing on separate lines):



```
Which base (2-10): 2
 0000
 0001
 0010
 0011
 0100
 0101

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)







Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)