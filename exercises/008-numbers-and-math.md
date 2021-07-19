# Numbers and Math

Every programming language has some kind of way of doing numbers and math. Don't worry, programmers lie frequently about being math geniuses when they really aren't. Although it helps to have a strong background in mathematics, high-level math doesn't enter into the daily life of an average software developer.


This exercise has lots of math symbols so let's name them right away so you know what they're called. As you type this one in, say the names. When saying them feels boring you can stop saying them. Here are the names:


| Symbol | Name | Operation |
| ------ | ---- | --------- |
| `+` | plus |  |
| `-` | minus |  |
| `/` | slash |  |
| `//` | double slash |  |
| `*` | asterisk |  |
| `%` | percent |  |


Notice how the "Operation" column is blank? After you type in the code for this exercise, figure out what each of these does and complete the table. For example, `+` does addition.

Create a file called:

`008_numbers_and_math.py`

```python
print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
print("there are " + str(33 - 11) + " boys.")
print()
print(f"That means {11 / 33} % are girls...")
print("and {} % are boys.".format((33 - 11) / 33))
print()
print("If we made groups of six...")
print(f"There would be {33 // 6} groups of six.")
print(f"And then a smaller group of {33 % 6} people.")
print("-" * 30)
print("If we had 17 apples and 3 people...")
print(f"Each person would get {17 // 3} whole apples.")
print("There would be " + str(17 % 3) + " apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
print("they would each pay ${}.".format(2 * 5))

```

What You Should See
-------------------

```
I have a class of 33 students.
There are 11 girls, so that means..
there are 22 boys.

That means 0.3333333333333333 % are girls...
and 0.6666666666666666 % are boys.

If we made groups of six...
There would be 5 groups of six.
And then a smaller group of 3 people.
------------------------------
If we had 17 apples and 3 people...
Each person would get 5 whole apples.
There would be 2 apples remaining.

If we charged each person $2 each for their 5 apples..
they would each pay $10.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will not receive any points.

1. Above each line with a mathematical operation, use the `#` symbol to write a comment to yourself explaining what the line does.
2. Look up Python's `round()` function and use it to round the percentages to two decimal places.
3. Python has a number of ways to format output strings. There is a mixture of all of them in the above code. Choose one you like best and modify all the string formatting to use that one.
	- f-strings
		- `f"Hello I am {2021 - 1984} years old."`
		- Result: `"Hello I am 37 years old."`
		- Injects the Python code directly into the string.
		- Good because it's easy to see the exact resulting string without much clutter.
	- "dot format"
		- `"{}-{}-{} {}:{} {}".format(2021, 9, 8, 2, 45, "pm")`
		- Result: `"2021-9-8 2:45 pm"`
		- Injects values based on the position of the `{}`.
		- Good to keep the template text free from clutter especially when you have a lot of values to insert.
	- Concatenation
		- `"Hello " + "I'm " + "your " + "teacher"`
		- Result: `"Hello I'm your teacher"`
		- Can be difficult to keep track of all the `"` and `+` symbols which could cause errors.



Frequently-Asked Questions
--------------------------
- How does modulus (`%`) work?
	- Another way to say it is, "X divided by Y with a remainder of J." As in, "100 divided by 16 with a remainder of 4." The result of `%` is the J part, or the remainder part.
- What is the order of operations?
	- In the United States we use an acronym called PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. That's the order Java follows as well.

---

©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)