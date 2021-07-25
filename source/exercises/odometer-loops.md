# Odometer Loops


Download the following code, and get it to run.


## Files Needed

* [odometer_loops.py](../_static/examples/odometer_loops.py)



```python
import time


for thous in range(0, 10):
    for hund in range(0, 10):
        for tens in range(0, 10):
            for ones in range(0, 10):
                print("{}{}{}{}\r".format(thous, hund, tens, ones), end="")
                time.sleep(0.01)

```

What You Should See
-------------------
... a number increasing on the same line.


What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. Change all the loops so that they count from `0` to `7` instead of
 `0` to `9`. This will display numbers in "octal" (base 8) instead of
 "decimal" (base 10).
2. Change the code so that the human gets to type in a number for the base, and your odometer counts up to that instead of `8`. You might want to increase the delay (put a bigger number (like maybe `0.5`) inside the `time.sleep()` function).

After you've made all the changes, it should look something like this
(except that all your numbers will be overwriting each other on the same
line instead of printing on separate lines):


```
Which base (2-10): 2
 0000
 0001
 0010
 0011
 0100
 0101
```

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)







Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)