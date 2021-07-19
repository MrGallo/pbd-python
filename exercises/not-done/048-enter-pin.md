# Enter Your PIN


Type in the following code, and get it to compile. This assignment will help you learn how
to make a loop, so that you can repeat a section of code over and over again!



```
import java.util.Scanner;

public class EnterPIN
{
	public static void main( String[] args )
	{
		Scanner keyboard = new Scanner(System.in);
		int pin = 12345;

		System.out.println("WELCOME TO THE BANK OF MITCHELL.");
		System.out.print("ENTER YOUR PIN: ");
		int entry = keyboard.nextInt();

		while ( entry != pin )
		{
			System.out.println("\nINCORRECT PIN. TRY AGAIN.");
			System.out.print("ENTER YOUR PIN: ");
			entry = keyboard.nextInt();
		}

		System.out.println("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.");
	}
}

```

What You Should See
-------------------



```
WELCOME TO THE BANK OF MITCHELL.
ENTER YOUR PIN: 90210

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 11111

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 12345

PIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.

```

Notice what happens when we type the correct PIN on the first try:



```
WELCOME TO THE BANK OF MITCHELL.
ENTER YOUR PIN: 12345

PIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
no credit.


1. How is a `while` loop similar to an `if` statement?
 - How is a `while` loop different from an `if` statement?
 - Inside the `while` loop, why isn't there an `int`
 in front of the line `entry = keyboard.nextInt()`?
 - Delete the line `entry = keyboard.nextInt();` from inside
 the `while` loop. What happens? Why?
 - (Put the `entry = keyboard.nextInt();` back before you turn in the assignment.)







```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)