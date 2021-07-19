# Your Schedule

Create a file called:

`013_your_schedule.py`

Use several variables to store the names of your classes and their teachers. Then, display a nice little table displaying your schedule. Just FYI, my column of courses has a width of `26` characters, and the teacher column has a width of `15`. The first and last lines are a plus sign, fifty dashes (a.k.a. minus signs) and another plus sign.

**Your table doesn't need to look exactly like this, or even line up**. I used a total of sixteen variables (`course1`, `course2`, ... `course8`, `teacher1`, `teacher2`, etc.). You should do the same.

Here is some f-string code that could help you line up your strings:
```python
# Python shell
>>> name = "Mr. Gallo"
>>> f"{name:>20}"
'           Mr. Gallo'
>>> f"{name:<20}"
'Mr. Gallo           '
```

Here is something similar for `.format()`:
```python
# Python shell
>>> name = "Mr. Gallo"
>>> "{:>20}".format(name)
'           Mr. Gallo'
>>> "{:<20}".format(name)
'Mr. Gallo           '
```

The `>` and `<` symbols in this instance point to where the the text will be aligned. The `20` means the total space taken up will be `20` characters. Python will automatically calculate how many spaces to put based on the size of the string you are injecting.

If things are not lining up perfectly, just skip it. Lining up text is one of the least important things to spend your time on right now.

```
+------------------------------------------------------------+
| 1 |                          English III |       Ms. Lapan |
| 2 |                          Precalculus |     Mrs. Gideon |
| 3 |                         Music Theory |       Mr. Davis |
| 4 |                        Biotechnology |      Ms. Palmer |
| 5 |           Principles of Technology I |      Ms. Garcia |
| 6 |                             Latin II |    Mrs. Barnett |
| 7 |                        AP US History | Ms. Johannessen |
| 8 | Business Computer Infomation Systems |       Mr. James |
+------------------------------------------------------------+
```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)