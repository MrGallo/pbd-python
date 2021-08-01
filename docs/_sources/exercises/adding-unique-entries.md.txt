# Adding Unique Entries

Create a program that will read in a JSON database file, then add an entry using user input, the overwrite the file saving that new entry.

The database is a single dictionary composed of student dictionaries. A dict of dicts. Each key in the database dictionary is a `student_id` and the value is a student dictionary.

Once loaded into Python it would look like:
```python
students = {
    "188759": {
        "name": "Neli Kustner",
        "grade": 12,
        "student_id": 188759,
        "points": 1878
    },
    "105277": {
        "name": "Carolien Amador",
        "grade": 12,
        "student_id": 105277,
        "points": 1416
    }
}
```

## What you should do
1. Create a `main` function along with an `if __name__ == "__main__"` guard.
2. Ask the user to enter a new student. Be sure to include `name`, `grade`, `student_id`, `points`.
3. Write the new database dictionary to the original file.
4. Create a function called `is_unique`. It will take a dictionary (the database) as well as a `student_id`. The purpose is to loop through the database dictionary's `.keys()` and return `True` if the given `student_id` is *not* in the database already. Essentially, if the id is unique, it returns `True`. Write a docstring for this function.
5. Use the `is_unique` function and disallow any user input that contains a duplicate `student_id`. More points for using the function in a validation loop. Keep the user trapped in the validation loop until they enter a usable `student_id`.
    ```
    Add a new student

    student_id: 12345
    Error: Student ID already in database.
    student_id: 12345
    Error: Student ID already in database.
    student_id: 12345
    Error: Student ID already in database.
    student_id: 99999
    name: Frank McGill
    ...
    ```

You can use the following file that is a JSON dictionary of student dictionaries referenced by their student ID.

```eval_rst
* :download:`students-by-id.json <examples/students-by-id.json>`
```

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>