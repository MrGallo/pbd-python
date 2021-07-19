# Letter at a Time


Did you know that using a loop, you can examine a String one letter at a time?
The two key built-in String methods are `length()` and `charAt()`.


* `length()` returns an `int`
 representing the total number of characters in the String
 (including punctuation and whitespace). For example, if
 the variable `str` contains the String `"hello"`, then `str.length()` will
 return `5`.

 * `charAt( int n )` returns the
 `n`th character (`char`)
 in the String. The character positions are zero-based, so
 if the variable `str` contains the String `"ligature"`, then `str.charAt(0)`
 will return `'l'`, and `str.charAt(4)`
 will return `'t'`.



## Files Needed


* [LetterAtATime.java](examples/LetterAtATime.java)


What You Should See
-------------------



```
What is your message? A man, a plan, a canal: Panama!

Your message is 31 characters long.
The first character is at position 0 and is 'A'.
The last character is at position 30 and is '!'.

Here are all the characters, one at a time:

	0 - 'A'
	1 - ' '
	2 - 'm'
	3 - 'a'
	4 - 'n'
	5 - ','
	6 - ' '
	7 - 'a'
	8 - ' '
	9 - 'p'
	10 - 'l'
	11 - 'a'
	12 - 'n'
	13 - ','
	14 - ' '
	15 - 'a'
	16 - ' '
	17 - 'c'
	18 - 'a'
	19 - 'n'
	20 - 'a'
	21 - 'l'
	22 - ':'
	23 - ' '
	24 - 'P'
	25 - 'a'
	26 - 'n'
	27 - 'a'
	28 - 'm'
	29 - 'a'
	30 - '!'

Your message contains the letter 'a' 10 times. Isn't that interesting?

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
half credit or less.


1. The `for` loop is defined so that it repeats as long as
 `i < message.length()`. Try changing it to `<=`.
 What happens? Answer in a comment, then change it back.

 - If a string variable contains the value `"box"`,
 what is its `length()`? What is the position of the last character
 (the `'x'`)?

 - So, why does the `for` loop repeat as long as
 `i < message.length()` instead of `i <= message.length()`?

 - Currently the code prints out the number of 'a's in the message. Change it
 so that it prints out the number of vowels (`a A e E i I o O u U`).






```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)