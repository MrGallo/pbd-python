# How Old Are You, Specifically?

Using `if` statements, `elif`,
and `else` statements, make a program which displays
a different message depending on the age given.


| age | message |
| - | - |
| less than `16` | `"You can't drive."` | 
| `16` to `17` | `"You can drive but not vote."` | 
| `18` to `20` | `"You can vote but not rent a car."` | 
| `21` or older | `"You can do pretty much anything."` |


Note that unlike the [original "How
Old Are You" assignment](how-old-are-you.md), this program must only display *exactly one* message for a given age and not multiple messages.

Name your file:

`how_old_specifically.py`

```
Hey, what's your name? (Sorry, I keep forgetting): Billy Corgan
Ok, Billy Corgan, how old are you? 17

You can drive but you can't vote, Billy Corgan.
```

```
Hey, what's your name? (Sorry, I keep forgetting): Billy Corgan
Ok, Billy Corgan, how old are you? 14

You can't drive, Billy Corgan.
```

You can make up your own messages if you want, but you must have
at least four messages, and you must use `else if`
statements to make sure only one of the messages is printed for any
given age.



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)