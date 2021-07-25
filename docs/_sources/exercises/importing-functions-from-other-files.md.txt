# Importing Functions from Other Files

Rewrite the [Weekday Calculator](103-weekday-calculator.html) to have almost no functions in it. Start by opening up your solution to it (it should be called `weekday_calculator.py`) and saving a copy of it as `111_importing_functions.py`.


Then erase all the functions except for `main()` `is_leap()` and `weekday()`.

Now, when you run it, you should get a lot of errors about undefined functions.

To fix this, all we need to do is import those specific functions from files they are in. A big problem is we are technically not supposed to name Python files with number prefixes and when we try to import the files, we are going to get an error.

First, locate and rename the files we need to import:
| Before | After |
| - | - |
| `weekday_name.py` | `weekday_name.py` |
| `month_name.py` | `month_name.py` |
| `month_offset.py` | `month_offset.py` |


At the top of your `importing_functions.py` file, let's import those freshly named files:

```python
import weekday_name
import month_name
import month_offset
```

Please note that `weekday_name` actually refers to the file as a module (like the `math` module) which can contain multiple functions. It's just coincidence that the files only contain one function that happen to have the same name as the file. To actually call those functions in those modules, we need to reference the module first, then call the actual function:

```python
#   The module (file)
#   |           The name of the function IN the module.
#   v           v
weekday_name.weekday_name() 
month_name.month_name()
month_offset.month_offset()
math.sqrt()  # same idea. math module, sqrt function
```

Rename the function calls in your `importing_functions.py` to look like those shown just above.

*Note*: If those files lack the magical `if __name__ == "__main__"...`, when you import them you will actually run that file. We don't want that, we just want to use the specific function.

---

©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)