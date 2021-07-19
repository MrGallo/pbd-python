# Counting with a For Loop


As you saw in [Counting with a While Loop](counting-while.html),
a `while` loop can be used to to make something happen an
exact number of times.


However, this isn't our best choice. `while` loops are
designed to keep going *as long as* something is true. But if we know
in advance how many times we want to do something, Java has a special kind of
loop designed just for making a variable change values: the `for`
loop.


Type in the following code, and get it to compile. Then answer the
questions down below.



```
import java.util.Scanner;

public class CountingFor
{
    public static void main( String[] args )
    {
        Scanner keyboard = new Scanner(System.in);

        System.out.println( "Type in a message, and I'll display it five times." );
        System.out.print( "Message: " );
        String message = keyboard.nextLine();

        for ( int n = 1 ; n <= 5 ; n = n+1 )
        {
            System.out.println( n + ". " + message );
        }

    }
}

```

`for` loops are best when we know in advance how many times we want to do something.


* Do this ten times.
 * Do this five times.
 * Pick a random number, and do it that many times.
 * Take this list of items, and do it one time for each item in the list.





On the other hand, `while` loops are best for repeating *as long as*
something is true:


* Keep going as long as they haven't guessed it.
 * Keep going as long as you haven't got doubles.
 * Keep going as long as they keep typing in a negative number.
 * Keep going as long as they haven't typed in a zero.





What You Should See
-------------------



```
Type in a message, and I'll display it five times.
Message: Hey, hey.
1. Hey, hey.
2. Hey, hey.
3. Hey, hey.
4. Hey, hey.
5. Hey, hey.

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
no credit.


1. What does `n = n+1` do? Remove it and see what happens. (Then put it back.)
 - What does `int n = 1` do? Remove it and see what happens. (Then put it back.)
 - Change the code so that the loop repeats ten times instead of five.
 - See if you can change the for loop so that the message starts at 2 and counts by twos, like so:


```
Type in a message, and I'll display it ten times.
Message: qwerty
2. qwerty
4. qwerty
6. qwerty
8. qwerty
10. qwerty

```







```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)