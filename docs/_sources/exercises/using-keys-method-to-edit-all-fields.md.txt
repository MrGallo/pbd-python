# Using Keys Method to Edit All Fields

Download the starter code and get it to run. It should ask you to change the fields in the student dictionary, but it won't actually change anything.

```eval_rst
* :download:`using_keys_method_to_edit_all_fields.py <examples/using_keys_method_to_edit_all_fields.py>`
```

## What you should see
```
Please enter new values for the following:

student_id: 12
name: Johnny
grade: 11
average: 95

STUDENT INFO:

student_id: 123
name: John
grade: 10
average: 88.0
```


## What you should do
1. In the first loop, after you get `new_value` from the user, assign it to its proper place in the dictionary. Use the `key` variable to access the appropriate field. The program should show the following:
    ```
    Please enter new values for the following:

    student_id: 555
    name: Goku
    grade: 99
    average: over 9000

    STUDENT INFO:

    student_id: 555
    name: Goku
    grade: 99
    average: over 9000
    ```
2. Let's pretend that we don't want the `student_id` to be changed. In the loop, prevent that field from being changed. Use the `continue` statement to skip to the next loop iteration if the `key` is `"student_id"`.
3. You will notice that all new values come in as strings and therefore will change the grade and average for the student to strings. We don't want this. Use an if statement in the input-loop to check the type of each original item and do the appropriate conversion *before saving the new value to the dictionary*.
    ```python
    if type(student[key]) is int:
        # convert the new value to an int.
    ```
    The types to check for are `str`, `int`, and `float`. Use the `int()` and `float()` functions to do the conversions if necessary.

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>