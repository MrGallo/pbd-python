# Weekday Calculator


Using the functions you wrote in previous assignments and
the leap year function provided, write a function to determine the
day of the week a person was born given his or her birthday. The
following steps should be used to find the day of the week
corresponding to any date from 1901 through the present.

In the following explanation, the following terms will be helpful.
Assuming I type in a birthday as `"6 10 1981"`:


- The *month* is `6`.  
- The *day of the month* is `10`.  
- The *year* is `1981`.

* [103_weekday_calculator.py](examples/103_weekday_calculator.py)

Instructions
------------
*Tip*: I would comment-out the input section and leave the "automatic tests". This way, when you run the program you don't need to waste time typing anything in. The tests will tell you if your function is working or not. When you are convinced that it is working, you can uncomment that input section to turn the assignment in.

**First**, paste in your `month_name`, `weekday_name`, and `month_offset` functions from your previous exercises.

In the `weekday` function:
1. Find the number of years since `1900`, and put it into a variable called `years_since_1900`. Simply subtract `1900` from the year (`yyyy`) to get this.
2. Divide the number of years since `1900` by `4`. Put the quotient in a variable called `total`. For example, if the person was born in `1983`, `years_since_1900` would be `83`. Divide `83` by `4` and store `20` in `total`. The result must be an integer, so use floor division.
3. Also add the number of years since `1900` to `total`.
4. Add the day of the month to `total`, but because we need to `0`-index the day of the month, we need to also subtract `1`.
5. Using the function `month_offset()` you wrote, find the "month offset" and add it to `total`.
6. If the year is a leap year and if the month you are working with is either January or February, then subtract `1` from the `total`. You can use the function `is_leap()` provided to determine if the year is a leap year.
7. Find the remainder when `total` is divided by 7. Pass this remainder to the function `weekday_name()` you wrote to determine the day of the week the person was born. Store this in a variable called `weekday`.
8. Finally, build up a single String value containing the whole date (day of week, month, day, year). You'll need to use the function `month_name()` you wrote to show the month name rather than its number.
9. Return that String value.


Whew. Here's some code to get you started.

```
Welcome to Mr. Mitchell's fantastic birth-o-meter!

All you have to do is enter your birthday, and it will tell you
the day of the week on which you were born.

Some automatic tests....
12 10 2003 => Wednesday December 10, 2003
 2 13 1976 => Friday February 13, 1976
 2 13 1977 => Sunday February 13, 1977
 7  2 1974 => Tuesday July 2, 1974
 1 15 2003 => Wednesday,January 15, 2003
10 13 2000 => Friday October 13, 2000

Now it's your turn!  What's your birthday?
Birthday (mm dd yyyy):
mm: 11
dd: 11
yyyy: 2010

You were born on Thursday November 11, 2010!

```

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)