# Baby Nim

Write a program that starts with three "piles" of 3 counters each. Let the player choose piles and remove counters until all the piles are empty.

1. Start by placing counters (coins or toothpicks or something) into 3 piles.
2. The player picks a pile, then removes one or more counters from that pile. (It's okay to take the whole pile.)
3. The player picks a new pile, then removes one or more counters from that pile. (It's okay to pick the same pile as before.)
4. Once all piles are empty, the game stops.

You do not need to check for errors like a wrong pile name, or if someone tries to take more counters from the pile than the pile has.

Name your file `063b_baby_nim.py`

Sample Output
-------------
```
A: 3	B: 3	C: 3

Choose a pile: A
How many to remove from pile A: 2

A: 1	B: 3	C: 3

Choose a pile: C
How many to remove from pile C: 3

A: 1	B: 3	C: 0

Choose a pile: B
How many to remove from pile B: 1

A: 1	B: 2	C: 0

Choose a pile: A
How many to remove from pile A: 1

A: 0	B: 2	C: 0

Choose a pile: B
How many to remove from pile B: 1

A: 0	B: 1	C: 0

Choose a pile: C
How many to remove from pile C: 2

A: 0	B: 1	C: -2

Choose a pile: B
How many to remove from pile B: 1

A: 0	B: 0	C: -2

All piles are empty. Good job!
```

---


©2013 [Graham Mitchell](https://programmingbydoing.com/)


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)
