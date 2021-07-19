# Asking Questions


It's now time to pick up the pace a bit. I've got you doing a lot of
printing so that you get used to typing simple things, but those simple
things are fairly boring. What we want to do now is get you getting data
into your programs. This though is a little tricky so we have to have
you learn to do two things that may not make sense right away, but if
you stick with it they should click suddenly a few exercises from now.


Most of what software does is the following:


1. Take some kind of input from a person.
 - Change it.
 - Print out something to show how it changed.




So far you've only been printing, but you haven't been able to get any
input from a person, or change it. You may not even know what "input"
means, so rather than talk about it, let's have you do some and see if
you get it. Next exercise we'll do more to explain it.



```
import java.util.Scanner;

public class AskingQuestions
{
	public static void main( String[] args )
	{
		Scanner keyboard = new Scanner(System.in);

		int age;
		String height;
		double weight;

		System.out.print( "How old are you? " );
		age = keyboard.nextInt();

		System.out.print( "How tall are you? " );
		height = keyboard.next();

		System.out.print( "How much do you weigh? " );
		weight = keyboard.nextDouble();

		System.out.println( "So you're " + age + " old, " + height + " tall and " + weight + " heavy." );
	}
}

```

Notice that we used print instead of println. This is so that the program
doesn't end the line with a newline and go to the next line.


What You Should See
-------------------



```
U:\My Documents\CompSci\>java AskingQuestions
How old are you? 35
How tall are you? 6'2"
How much do you weigh? 180
So, you're 35 old, 6'2" tall and 180 heavy.

U:\My Documents\CompSci\>

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will not receive
any points.


1. Change the program so that it reads in the height in two parts. The first part should
 read in an int for the number of feet. Then read in a second int
 for the number of inches. Try to make the output look the same, though.



```
How old are you? 35
How many feet tall are you? 6
And how many inches? 2
How much do you weigh? 180
So, you're 35 old, 6'2" tall and 180 heavy.

```


```



```



---


Copyright © 2010 Zed A. Shaw. Used by permission.


(The original Python version of this assignment is part of Zed Shaw's excellent 
[Learn Python the Hard Way](http://learnpythonthehardway.org/) course and
was translated to/reinterpreted for Java by Graham Mitchell.)




