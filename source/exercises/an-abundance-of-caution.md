# An Abundance of Caution

When we create functions for other developers to use, we should ensure they are passing the correct arguments to our functions. This will help guide them when they attempt to use our code.

1. Create a function that takes a percent values from `0.0` to `1.0` and converts it to a string from `"0%"` to `"100%"`. Use the `round()` function to make it appear with no decimal places.
2. Create a docstring for this function and write type annotations.
3. Create a `main` function that will make use of the percent conversion function.
4. Raise an exception in your function when it recieves a value outside its defined range (`0.0` to `1.0`). This is a reasonable check to perform.

If the programer using your function decides to ignore your docstring and annotation by passing a `str` insead of a `float`, that's really on them. Whatever side effect that comes from that is their responsibility. You could equip your function to check that issue as well...

5. Ensure your function recieves a `float` number. Raise an exception if not. Use Python's `type()` function. *Note: this is a different type of error than question #4.*


---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>