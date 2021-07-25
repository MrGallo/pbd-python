# Exchange Sort


Take your [exchange sort inner loop](exchange-sort-inner-loop.md) code and insert it in the following file in the appropriate loactions:

* [160_exchange_sort.py](../_static/examples/160_exchange_sort.py)

What to do
----------
1. Take the inner loop from the previous assignment and place it in the `exchange_sort` function.
2. There is a `swap` function already written for you. You must call that `swap` function from your `exchange_sort` function when it is required.
3. Nest your exchange sort inner loop inside of another loop that will be responsible for incrementing the `marker` variable from `0` the length of the list to be sorted.

```
before: 45 87 39 32 93 86 12 44 75 50
after : 12 32 39 44 45 50 75 86 87 93
```

Note, the starter code generates random numbers so your output will have different numbers, but should still be sorted by the end.

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)