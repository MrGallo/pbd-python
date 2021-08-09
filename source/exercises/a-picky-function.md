# A Picky Function

```eval_rst
* :download:`a_picky_function.py <examples/a_picky_function.py>`
```
Download and run the starter code. Initially it should run as shown.

```
My Special Addition Program
===========================

3 + 2 = 5
5 + 6 = 11
8 + -3 = 5
100 + 55 = 155
5 + 5 = 10
```

## What you should do
This function is supposed to raise an error if the two given numbers are the same. There is no reason for this outside of practice.

1. Create a custom error called `RefusalToAddTheSameNumberError`. Make sure it inherits from the base-class of `Exception`.
2. In the `picky_function`, if the two numbers are the same `raise` the custom function you created and give it a message of `"I refuse to add the same number to itself."`.

## What you should see
```
My Special Addition Program
===========================

3 + 2 = 5
5 + 6 = 11
8 + -3 = 5
100 + 55 = 155
Traceback (most recent call last):
  File "main.py", line 38, in <module>
    main()
  File "main.py", line 15, in main
    print(f"5 + 5 = {picky_sum(5, 5)}")
  File "main.py", line 33, in picky_sum
    raise RefusalToAddTheSameNumberError("I refuse to add the same number to itself.")
__main__.RefusalToAddTheSameNumberError: I refuse to add the same number to itself.
```