# Hi-Lo with Limited Tries


Write a program that picks a random number from `1-100`.
The user keeps guessing as long as their guess is wrong,
**and** they've guessed less than `7` times. If their
guess is higher than the number, say `"Too high."` If their guess
is lower than the number, say `"Too low."` When they get it right,
the game stops. Or, if they hit seven guesses, the game stops
even if they never got it right.


This means your `while` loop will have a compound condition using `and`.

Name the file: `hi_lo_limited.py`

```
I'm thinking of a number between 1-100.  You have 7 guesses.
First guess: 50
Sorry, you are too low.
Guess # 2: 75
Sorry, you are too low.
Guess # 3: 87
Sorry, that guess is too high.
Guess # 4: 82
Sorry, you are too low.
Guess # 5: 84
You guessed it!  What are the odds?!?

```

```
I'm thinking of a number between 1-100.  You have 7 guesses.
First guess: 1
Sorry, you are too low.
Guess # 2: 2
Sorry, you are too low.
Guess # 3: -8
Sorry, you are too low.
Guess # 4: 0
Sorry, you are too low.
Guess # 5: 7
Sorry, you are too low.
Guess # 6: 612
Sorry, that guess is too high.
Guess # 7: -523
Sorry, you didn't guess it in 7 tries.  You lose.

```

---

©2013 [Graham Mitchell](https://programmingbydoing.com/)


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)
