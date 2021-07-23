# Keychains for Sale


Write a program that pulls up a menu with 4 options. Name the file `108_keychains1.py`. It should look something like...

```
Ye Olde Keychain Shoppe

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 1

ADD KEYCHAINS

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 3

VIEW ORDER

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 4

CHECKOUT

```

* You will need to create functions for each of the 4 menu
 options. Entering the number will call the correct function.

 * Make use of a `main()` function for printing and menu input. Use `if __name__ == "__main__":`.

 * This assignment does not require you to complete ANY of the
 functionality except for the working menu system. *Each function should print a message that it has been called*. i.e., `"ADD KEYCHAINS"` or `"VIEW ORDER"`.

 * The functions should be named `add_keychains()`, `remove_keychains()`, `view_order()` and `checkout()`.

 * The user should be able to keep putting in choices until
 the checkout() function is called. When checkout() is finished,
 the program should end. Have the loop `break` or reach some terminating condition. *Do not use `exit()` or `-100` points*.


---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)