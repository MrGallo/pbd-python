# Age Messages 3

Using `if` statements with compound conditions
(like `and` and `or`), make a program that displays a single
message depending on the age given.


| age | message |
| - | - |
| less than `16` | `"You can't drive."`|
| `16` to `17` | `"You can drive but not vote."`|
| `18` to `24` | `"You can vote but not rent a car."`|
| `25` or older | `"You can do pretty much anything."` |



This output of this assignment is identical to [the "How
Old Are You, Specifically" assignment](025-how-old-are-you-elseif.md). However, this time you *must*
accomplish it using `if` statements with compound conditions and **you *must not* use `elif` or `else`**.

Name your file: `034-age-compound-boolean.py`


```
Your name: Dukes
Your age: 19

You can vote but you can't rent a car, Dukes.

```

 



```
Your name: Dukes
Your age: 12

You can't drive, Dukes.

```

You can make up your own messages if you want, but you must have at least four messages, and you must use the `and` operator to make sure only one of the messages is printed for any given age.


---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)