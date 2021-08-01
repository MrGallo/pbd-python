# Restructuring Database

Download this database of students:

```eval_rst
* :download:`student-points.json <examples/student-points.json>`
```

The database is stored as a list of dictionaries. Let's convert that structure to a dictionary of dictionaries. We will store all students in one dictionary called `students`. 

```python
students = {
    # ...
}
```

The `student_id` of each student in the original list will be the key. This is useful if we want to be able to quickly pull up a student by their id. We won't need to run any search algorithm.

```python
students = {
    "102356": {},  # student dict
    "185342": {},  # another student dict
}
```

If I wanted to pull up the student with id `102356`, I would just use `students[102356]`. Integers can be keys in dictionaries in Python. The trouble is, that's not the case for JSON - JSON keys must be strings (see below).

When you have restructured the data, write it to a file. It should look like (leaving out some entries for brevity):

```json
{
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
    },
    "136978": {
        "name": "Biff Van Rossem",
        "grade": 12,
        "student_id": 136978,
        "points": 2606
    }
}
```

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>