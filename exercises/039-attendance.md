# Attendance

Make a program that asks for the last name of the
user. Depending on their last name, make a statement about
how long they have to wait during roll call. You need to use
`elif`'s to make sure only one statement
gets printed.

Once you understand how comparing strings works using the comparison operators, this is a pretty straightforward assignment, much like [How Old Are You, specifically](025-how-old-are-you-elseif.md), except that it uses strings instead of `int`s.


* name is `"Carswell"` or before: say `"you don't have to wait long"`
* name is `"Jones"` or before: say `"that's not bad"`
* name is `"Smith"` or before: say `"looks like a bit of a wait"`
* name is `"Young"` or before: say `"it's gonna be a while"`
* name is after `"Young"`: say `"not going anywhere for a while?"`

Name your file: `039_attendance.py

```
What's your last name? Stephanopolis
It's gonna be a while, "Stephanopolis".
```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)