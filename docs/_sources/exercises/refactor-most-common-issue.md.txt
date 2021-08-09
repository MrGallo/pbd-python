# Refactor Most Common Issue

Here is classic beginner code. There is *way* too much in the `try` portion of the code. We don't need to *try* lines of code that have **zero** chance of raising an error.

```python
try:
    # Display menu options
    print("1 - Option One")
    print("2 - Option Two")
    print("3 - Option Three")
    print()

    # get choice
    choice = int(input("> "))

    # handle choice
    if choice == 1:
        print("You chose OPTION ONE.")
    elif choice == 2:
        print("You chose OPTION ONE.")
    elif choice == 3:
        print("You chose OPTION ONE.")
    else:
        print("Invalid option.")
except ValueError:
    print("Invalid option.")

```

## What you should do
1. Refactor the code to include **ONLY** the single line of code that could possibly raise an error. Some code needs to go outside *before* the `try/except` and some other code needs to go outside *after* the `try/except`.


---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>