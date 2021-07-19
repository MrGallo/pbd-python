# Else And If


Type this one in and make it work, too.



```
public class ElseAndIf
{
	public static void main( String[] args )
	{
		int people = 30;
		int cars = 40;
		int buses = 15;

		if ( cars > people )
		{
			System.out.println( "We should take the cars." );
		}
		else if ( cars < people )
		{
			System.out.println( "We should not take the cars." );
		}
		else
		{
			System.out.println( "We can't decide." );
		}


		if ( buses > cars )
		{
			System.out.println( "That's too many buses." );
		}
		else if ( buses < cars )
		{
			System.out.println( "Maybe we could take the buses." );
		}
		else
		{
			System.out.println( "We still can't decide." );
		}


		if ( people > buses )
		{
			System.out.println( "All right, let's just take the buses." );
		}
		else
		{
			System.out.println( "Fine, let's stay home then." );
		}

	}
}

```

What You Should See
-------------------



```
U:\My Documents\CompSci\>java ElseAndIf
We should take the cars.
Maybe we could take the buses.
All right, let's just take the buses.

U:\My Documents\CompSci\>

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive half credit or less.


In this section, you're going to try to guess what you think the if statement is and what it does.


1. What do you think else if and else are doing? Answer in a comment.
 - Remove the else part at the beginning of one of the else if statements.
 What difference does that make? Why? Answer in a comment.




```



```



---


Copyright © 2010 Zed A. Shaw. Used by permission.


(The original Python version of this assignment is part of Zed Shaw's excellent 
[Learn Python the Hard Way](http://learnpythonthehardway.org/) course and
was translated to/reinterpreted for Java by Graham Mitchell.)




