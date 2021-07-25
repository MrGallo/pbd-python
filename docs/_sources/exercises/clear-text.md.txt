# Clear text
Take your solution from the [previous exercise](favourite-colour.md) and add a button that will clear the text of all Entry widgets (name, age, and favourite colour).

You will need to:
- add the new "Clear" Button beside or below the "Submit" button.
    - Initialize (create) it, then call `.grid()` on it like the other widgets.
- add a `command` for the clear button `command=handle_clear` 
- Create the `handle_clear` function that will do the clearing.
- In the `handle_clear` function, you can call the `delete` method on each entry widget you want to clear.
    - E.g., `entry_name.delete(0, END)`

Name the file: `clear_text.py`

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)
