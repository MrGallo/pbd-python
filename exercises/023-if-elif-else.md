# If, Elif, Else

Type this one in and make it work, too.

Name your file:

`023_if_elif_else.py`

```python
team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")

```

What You Should See
-------------------
```
Team A wins!
Both Teams A and B have the same number of wins.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive half credit or less.

1. Why do you suppose the output says `"Both Teams A and B have the same number of wins."` when `team_a_wins` is initialized as only `15` and `team_b_wins` is initialized as `16`? It seems Team B has more wins. What is going on?
2. What do you think `elif` and `else` are doing? Answer in a comment.
3. Pick one of the `elif` statements and change it to `if` instead. What difference does that make? Why? Answer in a comment.


---

©2021 Daniel Gallo

This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)