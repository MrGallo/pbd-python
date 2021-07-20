# Randomness


You know what's cool? Having the computer randomly choose a number. This is the basis of pretty much every computer game ever.


To pick a random number, you first need to `import random`.


Then, you can use the [random library](https://docs.python.org/3/library/random.html)'s functions. The most useful, in my opinion is `random.randrange()`.


```python
import random


x = random.randrange(10)        # 0-9
y = random.randrange(5, 10)     # 5-9
z = random.randrange(5, 10, 2)  # 5-9, counting by two

# should be different every time you run the program
print(f"{x = }")
print(f"{y = }")
print(f"{z = }")
```

Starter code
------------
Name your file: `041_randomness.py`

```python
import random


x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")

print()
print("Here are some random numbers from 1 to 5...")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")
```

What You Should See
-------------------
Your random numbers will probably be different than these. Actually, that's kind of the point.

```
My random number is 8.

Here are some random numbers from 1 to 5...
3, 5, 1, 5, 5, 3, 2

Here are some random numbers from 1 to 100...
33, 57, 29, 29, 66, 30, 77, 78, 67, 8, 59

Will these next two random number be the same?
The two random numbers were different. Not too surprising.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. What happens if we change `random.randrange(1, 6)` to `random.randrange(1, 5)`? Make the change and run the program a few times to see the result. What seems to be the new range of numbers that pop up? 
2. After the `import` statement, use the `random.seed()` function and give it an integer like `random.seed(400)`. What do you notice? What happened to the random numbers?
3. Change to random seed to something else and observe the behavior. What happens to the random numbers?
4. There are a couple popular games I can think of that use this concept of a "seed". Why do you suppose they use it and what does it do in the game?

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)