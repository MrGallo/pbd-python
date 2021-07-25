# User Input

### IPO Model
Nearly every software application follows the **Input, Processing, Output** (IPO) Model. So far our programs have only covered **processing** (variable assignment, calculations, the *creation* of strings) and **output** (printing of strings to the terminal). From now on we will be writing programs that incorporate user **input** as well.

In Python this is accomplished using the `input()` function. When you run the program, it will actually pause and wait for you to type something in.

Manually write out the code below and run it. Name the file:

`user_input.py`

```python
print("Enter the following information about an item you wish to purchase..")
print()

print("The name of the item:")
name = input()

price = float(input("The price: $"))

print("How many do you want?")
quantity = int(input())

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")
```

What You Should See
-------------------
```
Enter the following information about an item you wish to purchase..

The name of the item:
Apples
The price: $0.50
How many do you want?
5

You choose to buy 5 Apples.
That will come out to $2.825
```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will not receive
any points.


1. What is different about how we took user input concerning the `price` as compared to how input was taken for the item `name`? There are two differences.
2. Because it looks better, make your user input for `name` and `quantity` also appear on the same line (like `price`).
3. What is a prompt? Why does switching the order as shown below cause a [usability](https://www.interaction-design.org/literature/topics/usability) issue?
	```python
	name = input()
	print("Enter the name of the item:")
	```
4. Explain the use of the `int()` and `float()` functions. Why are they used? What happens if you remove them? i.e., `price = input("The price: $")`
---

©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)
