# Serious Menu Error Handling

## Starter Code

```python
def main():
    # (label, function)
    menu_options = [
        ("First Option", first_option),
        ("Second Option", second_option),
        ("Third Option", third_option),
        ("Fourth Option", fourth_option),
    ]

    running = True
    while running:
        # display menu
        print("Choose an option.\n")
        for i, (label, function) in enumerate(menu_options):
            print(f"{i + 1} - {label}")
        print()
        print("'q' to quit")
        
        # Get choice
        choice = int(input("> ")) - 1

        # extract function from list
        label, function = menu_options[choice]

        # run the extracted function
        function()
        print()


def first_option():
    print("RUNNING FIRST OPTION")


def second_option():
    print("RUNNING SECOND OPTION")


def third_option():
    print("RUNNING THIRD OPTION")


def fourth_option():
    print("RUNNING FOURTH OPTION")


if __name__ == "__main__":
    main()
```

# What you should do
This program has some serious issues. It doesn't work properly and has the potential to raise a number of errors. Fix the following favouring `try/except` as much as possible. Your solution may refactor the code significantly, which is fine. Just preserve the concept of keeping the menu options in a list.

- `ValueError`: When the program gets the user choice and they enter a non-`int`.
- The program needs a way to quit when they enter a `'q'`.
- If the user enters a menu option `0` or lower, it will pick out the functions from the back. For example, if the user enters `0`, the program will subtract `1` to get `-1`, then it will pull out the function associated with `menu_options[-1]` which is the last menu option. This should not be allowed.
- `IndexError`: When the user enters a number higher than `4` and the program tries to access that index in the `menu_options` list.

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>