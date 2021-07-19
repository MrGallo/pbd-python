# Simple Web Input


In Java, reading text from a web page isn't much more difficult than reading
from a text file! Download the following code and get it to compile.


## Files Needed


* [SimpleWebInput.java](examples/SimpleWebInput.java)



```
**import** java.net.URL;
**import** java.util.**Scanner**;

**public class** SimpleWebInput
**{**
    **public static void** main**(****String****[]** args**)** **throws** **Exception**
    **{**
        URL mcool = **new** URL**(****"http://cs.leanderisd.org/mitchellis.txt"****)**;
        **Scanner** webIn = **new** **Scanner****(** mcool.openStream**() )**;

        **String** one = webIn.nextLine**()**;
        
        webIn.close**()**;
        
        **System**.out.println**(**one**)**;
    **}**
**}**

```

What You Should See
-------------------



```
Mr. Mitchell is cool.

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
half credit or less.


1. The code provided only reads a single line from the URL given,
 but `mitchellis.txt` contains two lines. Add in code
 to read in and display the second line as well.
 - Once that works, change the URL to read text from a different web location.




```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)