# Calling Functions from Other Files


Rewrite the [Weekday Calculator](weekday-calculator.html)
to have almost no functions in it. Start by opening up
`WeekdayCalculator.java` and saving a copy of it as
`CallingFunctionsFromOtherFiles.java`.


Then erase all the functions except for `main**()**`
and `weekday**()**`.


Now, when you compile it, you should get a lot of errors about
undefined functions.


Then rewrite all the function calls so that they refer to versions
in your previous assignments. The functions will be these:


* `MonthName.month_name()`* `WeekdayName.weekday_name()`* `MonthOffset.month_offset()`* `WeekdayCalculator.is_leap()`






```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)