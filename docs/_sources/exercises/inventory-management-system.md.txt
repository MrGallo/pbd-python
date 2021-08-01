# Inventory Management System

Create a program that will manage a store's product inventory. An inventory item is going to be a dictionary with the following format:

```python
item = {
    "sku": int,
    "name": str,
    "min_stock": int,
    "stock": int
}
```

Explanation of product keys:
- `"sku"`: [Stock Keeping Unit](https://www.investopedia.com/terms/s/stock-keeping-unit-sku.asp) or barcode. *Must be unique among all products*.
- `"stock"`: How many of the particular item we have available for sale.
- `"min_stock"`: The lowest stock level of the particular item before we trigger an automated order from the supplier.
- `"name"`: The name of the product.

Create a `main` function to display the following menu items:
1. Load inventory from file.
    - The user will choose the name of the databse file to open.
2. Display items in a table
    - `*` items that need to be ordered (optional)
    - order by alpha (optional)
3. Edit inventory item
    - Select a product by sku to edit its information.
4. Add inventory item
    - Prevent adding existing item.
5. Save changes to file.
6. Generate purchase-order
    - Scan through the database to determine if we need to order more of this product.

## Functions
You must create and make use of the following functions. Each must be fully type-annotated and docstrings written.
- `is_order_required`
- `show_tabbed`
- `set_name`
- `set_stock`
- `set_min_stock`

## `is_order_required`
This function will be given a single product (dictionary) and return `True` if we need to order more of this item. Need to compare the current stock level to the lowest allowed level.

## `show_tabbed`
Take a single product (dictionary) and print out it's information in a single row for printing in a table. You might want to draw from your function in [Fields in a Row](fields-in-a-row.md) for this.

## `set_name`
Given a product dictionary and a string to change the product's name, set the `"name"` key of the product. This function is going to ensure the name is a string that only contains letters and numbers (alpha-numeric). Use Python's built-in `str.isalnum()` method to determine this.

A *weak implementation* of this function will fail silently - i.e. it will fail to set the name without any indication.

A *strong implementation* of this function will raise an exception. There could be two potential errors that would fit this case. A `TypeError` and/or a `ValueError`.

## `set_stock`
Given a product dictionary and a string to change the product's stock level, set the `"stock"` key of the product. This function is going to ensure the new stock is actually an `int`. Furthermore, this number cannot be negative.

A *weak implementation* of this function will fail silently - i.e. it will fail to set the stock without any indication.

A *strong implementation* of this function will raise an exception. There could be two potential errors that would fit this case. A `TypeError` and/or a `ValueError`.

## `set_min_stock`
Given a product dictionary and a string to change the product's minimum stock level, set the `"min_stock"` key of the product. This function is going to ensure the new minimum stock value is actually an `int`. Furthermore, this number cannot be negative.

A *weak implementation* of this function will fail silently - i.e. it will fail to set the minimum stock level without any indication.

A *strong implementation* of this function will raise an exception. There could be two potential errors that would fit this case. A `TypeError` and/or a `ValueError`.

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>