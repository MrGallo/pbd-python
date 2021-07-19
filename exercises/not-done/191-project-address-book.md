# Project: Address Book


Write a program that functions as an address book. It should
have entries containing *at least* the following information: first
and last name, phone number, address, and email address. You should be
able to add entries and remove entries, as well as printing out any
given entry. It should save entries to a file, and be able to read in
entries from a file as well.


The address book must be able to sort by at least one field
(preferably last name). You may use any sort for this that you like.


The address book will almost certainly contain a fixed limit on the
total number of entries. However, it should be possible to increase
this limit by simply changing a single line in your program and then
recompiling with no other modifications.




---


An excellent program will be able to sort the entries by any field
(first name, last name, phone number, email address, etc).


An excellent program will be able to display only entries matching
a certain criteria (only last names beginning with the letter 'M', for
example).


An excellent program easily and intelligently handles the use
of multiple address books (multiple files).




---


A spectacular program features the ability to move an entry from one
address book to another.



```
1) Load from file
2) Save to file
3) Add an entry
4) Remove an entry
5) Edit an existing entry
6) Sort the address book
7) Search for a specific entry
8) Quit

Please choose what you'd like to do with the database:

```

Just a recommendation: use a variable to keep track of the
number of elements currently in the address book. This value
will increase when you add new entries and decrease when you
remove entries. This is the variable you will use in all
your `for` loops for iterating through the array of
records.


Once this variable reaches the capacity of the array
(`arr.length`), the address book is "full" and no new
entries can be added.



```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)