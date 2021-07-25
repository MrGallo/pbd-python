# Sorting an ArrayList of Records


Make a record to store information about a car. (This should seem
[familiar](reading-what-you-wrote.html).) It should contain fields
for:


* the make (String)
 * the model (String)
 * the year (int)
 * the license-plate number (String)





Create an ArrayList of `Car` objects.


Ask the user for the name of a file, and then open that file and read all that
data from that file into the ArrayList.


Finally, sort the ArrayList of cars by year and print them out.
(Note: Printing them the "easy" way won't work unless you've
added a `toString()` method to the Car object.)



```
From which file do you want to load this information? cars.txt
Data loaded.
Data sorted.

ArrayList: [1966 Ford Mustang (AZUCAR), 1980 Chevrolet Chevette (J43-SMB), 1985 Toyota Camry (622-VRX), 1993 Honda Civic (883-RS9), 1996 Dodge Neon (G74-LLC)]

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)