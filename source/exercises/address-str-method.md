# Address str Method


If you print out an object directly, you will get a rather confusing output. Let's give our `Address` class the ability to show us a better string representation of whatever `Address` obejct we we want to print. 

We will create a magic-method (dunder method) called `__str__` for the `Address` class that will return the string we want to show when we print the object.


What You Should See
-------------------
```
1. 191 Marigold Lane, Miami  33179
2. 3029 Losh Lane, Crafton  15205
3. 4939 Holt Street, Lake Worth  33463
4. 2693 Hannah Street, Hickory  28601
5. 4880 Carter Street, Fairview Heights  62208
```

## Files Needed

```eval_rst
* :download:`address_str_method.py <examples/address_str_method.py>`
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
half credit or less.

1. What happens if the function is renamed from `__str__` to something else? Answer in a comment, then change it back.
2. The `__str__` method given does not include the `state` field. Fix it so that it does.
3. What is `self` parameter that you see in the `__str__` method?
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)