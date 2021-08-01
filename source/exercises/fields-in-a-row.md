# Fields in a Row

Download and run the starter code:

```eval_rst
* :download:`fields_in_a_row.py <examples/fields_in_a_row.py>`
```

## What you should see
The program should start by printing out a table header, but crash when asked to print the row for the `car` dictionary. This is because you need to complete the `print_row` function.

```
make    model
----    -----
Traceback (most recent call last):
  File "main.py", line 21, in <module>
    print_row(car, fields)
TypeError: print_row() takes 0 positional arguments but 2 were given
```

## What you should do
1. Add parameters to the `print_row` function. The names and types are shown in the "Args" section of the docstring. Be sure to add type-annotations.
2. In the function, use a loop to iterate through the list of `fields` and print out each value from the dictionary on one line separated by a tab (`\t`). You should see:
    ```
    make    model
    ----    -----
    Toyota  Prius
    ```
3. Add `'color'` to the list of fields to display. The table should automatically print the color with the underline in the header as well as include the color in the row.
    ```
    make    model   color
    ----    -----   -----
    Toyota  Prius   grey
    ```
4. Add another field to the dictionary called `transmission` which can be either `"manual"` or `"automatic"`. Add this to the list of fields to display as well.

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>