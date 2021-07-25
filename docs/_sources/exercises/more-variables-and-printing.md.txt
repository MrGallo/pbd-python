# More Variables and Printing

In the last exercise we used f-strings to inject the variable values into the strings we wanted to print out. Here, we will make use of Python's other ways of achieving this using *[string interpolation](https://en.wikipedia.org/wiki/String_interpolation)* as well as [concatenation](https://en.wikipedia.org/wiki/Concatenation).

Name your file: `more_variables.py`

```
store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

print(f"At {store} I bought some {item}.")
print("They sold for $" + str(price) + " each.")
print("I wanted to purchase {} of them.".format(quantity))
print("The total price, with tax included, was ${total}.")
```

What You Should See
-------------------
```
At No Frills I bought some Apples.
They sold for $0.5 each.
I wanted to purchase 7 of them.
The total price, with tax included, was ${total}.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will not receive any points.

1. You will notice that the last line of output doesn't actually inject the `total` value into the string. What is missing in that line that is present in the first `print` line?
2. Above each `print` function call, write a comment telling me which formatting approach was used.
    - f-string
    - "dot format"
    - concatenation
3. Before the last line of output, include some output message(s) describing the `subtotal` and the `tax` amounts.
4. Change some of the variable values and observe how they alter the running of the program.

---

©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)

