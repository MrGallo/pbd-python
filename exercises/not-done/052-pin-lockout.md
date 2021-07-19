# PIN Lockout


Type in the following code, and get it to compile.



```
import java.util.Scanner;

public class PinLockout
{
	public static void main( String[] args )
	{
		Scanner keyboard = new Scanner(System.in);
		int pin = 12345;
		int tries = 0;

		System.out.println("WELCOME TO THE BANK OF MITCHELL.");
		System.out.print("ENTER YOUR PIN: ");
		int entry = keyboard.nextInt();
		tries++;

		while ( entry != pin && tries < 3 )
		{
			System.out.println("\nINCORRECT PIN. TRY AGAIN.");
			System.out.print("ENTER YOUR PIN: ");
			entry = keyboard.nextInt();
			tries++;
		}

		if ( entry == pin )
			System.out.println("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.");
		else if ( tries >= 3 )
			System.out.println("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.");
	}
}

```

What You Should See
-------------------



```
WELCOME TO THE BANK OF MITCHELL.
ENTER YOUR PIN: 10101

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 23232

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 99999

YOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
no credit.


1. Change the code so that it locks them out after 4 tries instead of 3.
 Make sure to change the message at the bottom, too.
 - Move the "maximum tries" value into a variable, and use that variable
 everywhere instead of just the number.




```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)