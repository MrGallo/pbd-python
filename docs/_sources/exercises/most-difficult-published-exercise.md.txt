# Most Difficult Published Exercise

Download the following files.

```eval_rst
* :download:`exercises-2.json <examples/exercises-2.json>`
* :download:`most_difficult_published.py <examples/most_difficult_published.py>`
```

If you run the Python file without the modifications, you will only see:

```
These are the most difficult dictionary exercises:
```

## What you should do
1. Call the `filter_difficult_and_published` function in `main` and pass it the `exercises` list. If you run the program here, it will display *all* the exercises. Not what we want.
2. Complete the `is_difficult` function. Read the doc string for what is considered "difficult" for this exercise.
3. Complete the `is_published` function. Complete the docstring for this function. It should return `True` if the `"published"` value in the given dictionary is `True`. False otherwise.
4. Complete the `filter_difficult_and_published` function. It recieves a list of dictionaries and returns a new list of all exercises that are *both* difficult *and* published. Make use of the `is_published` and `is_difficult` functions in here. Complete the docstring for this function.


## What you should see
```
These are the most difficult dictionary exercises:
    - Fields in a Row
    - Using Keys Method to Edit All Fields
    - Most Difficult Published Exercises
```

