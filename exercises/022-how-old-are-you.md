# How Old Are You?

Make a program which displays a different message depending on the age given. Here are the possible responses:


* age is less than `16`, say `"You can't drive."`
* age is less than `18`, say `"You can't vote."`
* age is less than `21`, say `"You can't rent a car."`
* age is `21` or over, say `"You can do anything that's legal."`

Here's a sample run. Notice that a person who is under `16` will
display *three* messages, one for being under `16`, one for also
being under `18`, and one for also being under `25`.

Name the file:

`022_how_old.py`

```
Hey, what's your name? Billy Corgan
Ok, Billy Corgan, how old are you? 17

You can't vote, Billy Corgan.
You can't rent a car, Billy Corgan.
```

What You Should Do on Your Own
------------------------------
1. Come up with a test plan that takes into account all possible outcomes of this program. Think of the IPO model. What inputs will result in what output? For example:
    
    |Input|Output|
    |-----|------|
    | `age = 17` | Can't vote, can't rent a car |
    
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)