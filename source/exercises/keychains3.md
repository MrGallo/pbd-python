# Keychains for Sale, real ultimate power


You're going to add some error checking and additional features, to [Keychains2](109-keychains2.html).

You need to make sure that the user always has a positive number, or `0`, of keychains in the order.

You need to check for a valid menu choice. If not, display an error message and show the menu again.

You will need 3 new variables in main, one to store the sales tax (`13%`), one to store the shipping cost per order (`$5.00`), and one to store the extra shipping cost for each additional keychain (`$1.00`).


`view_order(`) will need to be passed the three additional
variables, a total of five, and have a return type of `None`. It will
display, on different lines, the number of keychains in the order,
the price per keychain, the shipping charges on the order, the
subtotal before tax, the tax on the order, and the final cost of
the order.


`view_order()` might need to look like:

```python
def view_order(num_keychains: int, price_per_keychain: float, tax: float, base_shipping: int, per_keychain_shipping: int ) --> None:
```

`checkout()` will need to be passed the same values as `view_order()`, and have a return type of `None`. It will ask the user for his/her name in order to deliver them correctly, then call `view_order()` to display the order information, and then thank the user, by name, for ordering.


---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)