# PIN Lockout

Type in the following code, and get it to run.

Name the file: `052_pin_lockout.py`

```python
PIN = "12345"
tries = 0

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < 3:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= 3:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")
```

What You Should See
-------------------

```
WELCOME TO THE BANK OF GALLO.
ENTER YOUR PIN: 90210

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 11111

INCORRECT PIN. TRY AGAIN.
ENTER YOUR PIN: 54321

YOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. Change the code so that it locks them out after `4` tries instead of `3`. Make sure to change the condition at the bottom, too.
2. Make a variable (constant) for the number of maximum tries allowed. Use that variable everywhere instead of just the number.

---

©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)