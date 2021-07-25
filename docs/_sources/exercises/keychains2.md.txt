# Keychains for Sale, for real this time


Okay, now it is time to make the [keychain shop](keychains1.md) actually work.



```
Ye Olde Keychain Shoppe

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 1

You have 0 keychains. How many to add? 3
You now have 3 keychains.

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 2

You have 3 keychains. How many to remove? 1
You now have 2 keychains.

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 3

You have 2 keychains.
Keychains cost $10 each.
Total cost is $20.

1. Add Keychains to Order
2. Remove Keychains from Order
3. View Current Order
4. Checkout

Please enter your choice: 4

CHECKOUT

What is your name? Biff
You have 2 keychains.
Keychains cost $10 each.
Total cost is $20.
Thanks for your order, Biff!

```

* You will need 2 new variables in main, one to store the
 current number of keychains, and one to store the price per
 keychain.

 * The price should be `$10` per keychain.

 * `add_keychains()` will need to be passed one `int`, and have a
 return type of `int`. It will ask the user for the number of keychains
 to add to the order, and then return the new number of keychains.

 * `remove_keychains()` will need to be passed one `int`, and
 have a return type of `int`. It will ask the user for the number
 of keychains to remove from the order, and then return the new
 number of keychains.

 * `view_order()` will need to be passed two `int`s, and have a
 return type of `None`. It will display, on three different lines,
 the number of keychains in the order, the price per keychain,
 and the total cost of the order.

 * `checkout()` will need to be passed two `int`s, and have a
 return type of `None`. It will ask the user for his/her name in
 order to deliver them correctly, display the order information,
 and then thank the user, by name, for ordering.








```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)