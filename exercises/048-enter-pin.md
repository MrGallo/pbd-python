# Enter Your PIN


Type in the following code, and get it to compile. This assignment will help you learn how
to make a loop, so that you can repeat a section of code over and over again!

Name your file: `048_pin.py`

```python
PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

```

What You Should See
-------------------

```
WELCOME TO THE BANK OF GALLO.
ENTER YOUR PIN: 90210

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 11111

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 12345

PIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.
```

Notice what happens when we type the correct PIN on the first try:

```
WELCOME TO THE BANK OF GALLO.
ENTER YOUR PIN: 12345

PIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
no credit.

1. How is a `while` loop similar to an `if` statement?
2. How is a `while` loop different from an `if` statement?
3. What would we have to change in our program if the `PIN` was stored as an integer rather than a string? For example if it was initialized as `PIN = 12345`.
4. Comment out the line `entry = input(...)` from inside the `while` loop. What happens? Why?
5. (Uncomment the `entry = input(...)` before you turn in the assignment.)







```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)