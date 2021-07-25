# Storing Data in a File


Make a record to store information about a car. It should contain
fields for:


* the make, which is a string
 * the model, which is a string
 * the year, which is an integer
 * the license-plate number, which is a string





Create an array of type `Car` with five slots. Have
the user type in values to fill up the array.


Ask the user for the name of a file, and then open that file and
output all the data from the array to that file.


Use Notepad or some other text editor to confirm that the data
is correctly in the file. Be careful to only put *data* in the
file, and not labels.



```
Car 1
	Make: Toyota
	Model: Camry
	Year: 1985
	License: 622-VRX

Car 2
	Make: Chevrolet
	Model: Chevette
	Year: 1980
	License: J43-SMB

Car 3
	Make: Honda
	Model: Civic
	Year: 1993
	License: 883-RS9

Car 4
	Make: Ford
	Model: Mustang
	Year: 1966
	License: AZUCAR

Car 5
	Make: Dodge
	Model: Neon
	Year: 1996
	License: G74-LLC

To which file do you want to save this information? cars.txt

Data saved.

```

After you have run the program, the file cars.txt (or whatever you called it)
should look like this:



```
Toyota Camry 1985 622-VRX
Chevrolet Chevette 1980 J43-SMB
Honda Civic 1993 883-RS9
Ford Mustang 1966 AZUCAR
Dodge Neon 1996 G74-LLC

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)