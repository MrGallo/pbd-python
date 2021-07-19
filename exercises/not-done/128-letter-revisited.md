# Letter Revisited


Rewrite [A Letter to Yourself](letter-to-yourself.html),
but modify it so that instead of displaying the letter on the screen,
it puts it in a file.


When you run your program, it will appear to do nothing. But if you
wrote it correctly, it should have created a file in your home directory
called "letter.txt"  which you can then view
using a text editor.


What You Should See
-------------------



```


```

But then, after running your program, we can find and open this new file like so:



![screenshot of letter.txt opened in Notepad](examples/letter.png)

Frequently-Asked Questions
--------------------------



My program creates letter.txt, but it is empty/blank. Why?
You probably forgot to `close()` the file....


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)