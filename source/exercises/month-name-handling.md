# Month Name Handling

Continuing on from the previous exercise [Modify Month Name](modify-month-name.md), implement a validation loop with `try/except` to handle the error raised by your modified `month_name` function.

## What you should do
1. Create a `main` function to ask the user for a month number.
2. Attempt to pass the choice to the `month_name` function even if it is an invalid month number.
3. Take note of the error that it causes when given an invalid month number and set up a `try/except` structure to handle that particular error. In the except, simply state that the option they entered was invalid.
4. Use a loop to force the user to enter a valid number. It should not quit until they enter one.
    ```
    Enter a month number: 55
    Invalid number. Pick 1-12

    Enter a month number: 13
    Invalid number. Pick 1-12

    Enter a month number: 0
    Invalid number. Pick 1-12

    ...
    ```
5. Include in your `try/except` the ability to handle the error that occurs when the user enters a string value instead of a valid `int`.

---

©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>