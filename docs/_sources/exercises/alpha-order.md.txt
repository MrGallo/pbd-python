# Alpha Order


Write a program that compares several strings using the comparison operators `<` and `<`. You should display the strings and display the Boolean evaluation (`True` or `False`) that the comparison gives you.


Produce:
- 5 examples of two words where the first word comes before the second word in alphabetical order.
- 5 examples of two words where the first word comes after the second word.

You may **not** just flip the strings around; you must have ten *different* examples.

Name your file: `alpha_order.py`

Here's an example:

```python
# showing two different interpolation options.
# choose one that works best for you.
print(f"'axe' comes before 'dog': {'axe' < 'dog'}")
print("'{}' comes before '{}': {}".format("applebee's", "apple", "applebee's" < "apple"))
```


```
'axe' comes before 'dog': True
'applebee's' comes before 'apple': False
```

What to think about
-------------------
1. Why does `"Dog"` come before `"axe"`?
2. How can you fix this issue?

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)