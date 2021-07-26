# Counting with a While Loop


Type in the following code, and get it to run. This assignment shows you
how we can use a `while` loop to make something repeat an
exact number of times.

Name the file: `counting_while.py`

```python
print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

n = 0
while n < 5:
    print(f"{n + 1}. {message}")
    n += 1
```

Normally, `while` loops are best for repeating *as long as*
something is true:

* Keep going as long as they haven't guessed it.
* Keep going as long as you haven't got doubles.
* Keep going as long as they keep typing in a negative number.
* Keep going as long as they haven't typed in a zero.

But sometimes, we know in advance how many times we want to do something.

* Do this ten times.
* Do this five times.
* Pick a random number, and do it that many times.
* Take this list of items, and do it one time for each item in the list.

We can do that sort of thing with a `while` loop, but we have
to use a counter. A counter is a number variable (`int`) that starts with a value of `0`, and then we add `1` to it whenever something happens. So, here, we're going to be adding `1` to the counter everytime we repeat the loop. And when the counter reaches a predetermined value, we'll stop looping.


What You Should See
-------------------

```
Type in a message, and I'll display it five times.
Message: I will not swear in class

1. I will not swear in class
2. I will not swear in class
3. I will not swear in class
4. I will not swear in class
5. I will not swear in class
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. What does `n += 1` do? Remove it and see what happens. (Then put it back.) `ctrl + c` may come in handy.
2. Change the code so that the loop repeats ten times instead of five.
3. See if you can change the code so that the message still prints ten times, but the numbers in front count by tens, like so:

	```
	Type in a message, and I'll display it ten times.
	Message: I'm sending out an S.O.S.

	10. I'm sending out an S.O.S.
	20. I'm sending out an S.O.S.
	30. I'm sending out an S.O.S.
	40. I'm sending out an S.O.S.
	50. I'm sending out an S.O.S.
	60. I'm sending out an S.O.S.
	70. I'm sending out an S.O.S.
	80. I'm sending out an S.O.S.
	90. I'm sending out an S.O.S.
	100. I'm sending out an S.O.S.
	```
4. Change the code so that it asks the person how many times to display the message. Then, print it that many times. Still count by tens.
	```
	Type in a message, and I'll display it several times.
	Message: HELLO! My name is Inigo Montoya. You killed my father; prepare to die.

	How many times? 3
	10. HELLO! My name is Inigo Montoya. You killed my father; prepare to die.
	20. HELLO! My name is Inigo Montoya. You killed my father; prepare to die.
	30. HELLO! My name is Inigo Montoya. You killed my father; prepare to die.
	```

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)