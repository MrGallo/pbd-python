# Summing Several Numbers from Any File


Create a few more files in Notepad containing some integers
separated by some whitespace. Save them in your home directory as
`4nums.txt`, `5nums.txt`, `6nums.txt`, etc.


Then write a program that asks the user which file to open.
Then it should open that file, and read in and total up all the
integers from that file.


You won't be able to store each number in its own variable anymore.
Instead, you'll need to use a loop, and reuse the same variable over
and over. You'll have to add up the numbers as you go.
You've [done this before](adding-values-in-a-loop.md).

Name your file `sum_many_from_file.py`

```
Which file would you like to read numbers from: 5nums.txt 
Reading numbers from "5nums.txt"
 
1 2 3 4 5
Total is 15
```


```
Which file would you like to read numbers from: 8nums.txt 
Reading numbers from "8nums.txt"
 
3 1 4 1 5 9 2 6
Total is 31
```

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)