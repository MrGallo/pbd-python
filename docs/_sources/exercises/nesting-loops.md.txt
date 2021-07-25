# Nesting Loops


In programming, the term "nested" usually means to put something inside
the same thing. "Nested loops" would be one loop inside the
another one. If you do it right, then means the inner loop will repeat
*all* its iterations every time the outer loop does *one*
more iteration.


Start by downloading the following code, and get it to run.

## Files Needed

```eval_rst
* :download:`nesting_loops.py <examples/nesting_loops.py>`
```



```python
def main():

    # this is #1 - I'll call it "CN"
    for c in ('A', 'B', 'C', 'D', 'E'):
        for n in range(1, 4):
            print(f"{c} {n}")


    print("\n")

    # this is #2 - I'll call it "AB"
    for a in range(1, 4):
        for b in range(1, 4):
            print(f"{a}-{b} ", end="")
        # You will add a line of code here.

    print("\n")


if __name__ == "__main__":
    main()
```

What You Should See
-------------------

```
A 1
A 2
A 3
B 1
B 2
B 3
C 1
C 2
C 3
D 1
D 2
D 3
E 1
E 2
A 3


1-1 1-2 1-3 2-1 2-2 2-3 3-1 3-2 3-3


```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. Look at the first set of nested loops (`"CN"`). Which variable
 changes faster? Is it the variable controlled by the outer loop
 (`c`) or the variable controlled by the inner loop (`n`)? Answer in a comment.
2. Change the order of the loops so that the `"c"` loop is on the inside  and the `"n"` loop is on the outside. How does the output change?
3. Look at the second set of nested loops (`"AB"`). Remove the `end` override in the `print()` function:
    ```
    end=""
    ``` 
    How does the output change? (Then put it back.)
4. Add a print() function after the close brace of the inner loop (the `"b"` loop), but still inside the outer loop. How does the output change?

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)