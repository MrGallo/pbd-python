# No Negative Args, Please!

Download and run the starter code.

```eval_rst
* :download:`no_negative_args.py<examples/no_negative_args.py>`
```

## What you should see
```
3 items at $2.99 each is:
$8.97
```

## What you should do
1. In the `main` function, make the `item_price` a negative number. i.e., `-2.99`. Run the program and explain what happens. Answer the following in a comment.
    - What is the error?
    - What is the message?
    - On what line does the error occur?
    - What caused the error?
2. In the `calc_subtotal` function, add a check for the `quantity` value. Quantities cannot be negative so also raise a `ValueError` if the `quantity` is negative. In the main function fix the `item_price` variable to make it positive and make the `quantity` negative to observe the error.
3. In the `main` function, make both `item_price` and `quantity` negative. What do you see and what do you not see. Explain in a comment.
---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>