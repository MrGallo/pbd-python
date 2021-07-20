# Collatz Sequence


Take any natural number *n*.


* If *n* is even, divide it by 2 to get *n* / 2.
* If *n* is odd, multiply it by 3 and add 1 to get 3*n* + 1.
* Repeat the process indefinitely.


In 1937, Lothar Collatz proposed that no matter what number you begin with,
the sequence eventually reaches 1. This is widely believed to be true, but
has never been formally proved.

Write a program that inputs a number from the user, and then displays
the Collatz Sequence starting from that number. Stop when you reach 1.

Name your file: `062_collatz_sequence.py`

Sample Output
-------------
Here's an example of the expected output, assuming I start with 6 and
print tabs between each number.

```
Starting number: 6
6     3      10     5      16     8      4      2     1

```

Or, starting with a different number:

```
Starting number: 11
11    34    17    52    26    13    40    20    10    5
16    8     4     2     1

```

Some numbers take quite a while to reach 1:

```
Starting number: 27
27    82    41    124   62    31    94    47    142   71214   107   322   161   484   242   121   364   182   91274   137   412   206   103   310   155   466   233   700350   175   526   263   790   395   1186  593   1780  890445   1336  668   334   167   502   251   754   377   1132566   283   850   425   1276  638   319   958   479   1438719   2158  1079  3238  1619  4858  2429  7288  3644  1822911   2734  1367  4102  2051  6154  3077  9232  4616  23081154  577   1732  866   433   1300  650   325   976   488244   122   61    184   92    46    23    70    35    10653    160   80    40    20    10    5     16    8     42     1
```

Bonus #1 - Count Steps
----------------------
For +10 bonus points, also display the total number of steps in the sequence.

```
Starting number: 11
11    34    17    52    26    13    40    20    10    5
16    8     4     2     1

Terminated after 14 steps.
```


```
Starting number: 27
27    82    41    124   62    31    94    47    142   71214   107   322   161   484   242   121   364   182   91274   137   412   206   103   310   155   466   233   700350   175   526   263   790   395   1186  593   1780  890445   1336  668   334   167   502   251   754   377   1132566   283   850   425   1276  638   319   958   479   1438719   2158  1079  3238  1619  4858  2429  7288  3644  1822911   2734  1367  4102  2051  6154  3077  9232  4616  23081154  577   1732  866   433   1300  650   325   976   488244   122   61    184   92    46    23    70    35    10653    160   80    40    20    10    5     16    8     4    2     1

Terminated after 111 steps.

```

Bonus #2 - Largest Value
------------------------
For +20 bonus points, display the largest value encounted in the sequence.

```
Starting number: 11
11    34    17    52    26    13    40    20    10    5
16    8     4     2     1

The largest value was 52.

```



```
Starting number: 27
27    82    41    124   62    31    94    47    142   71
214   107   322   161   484   242   121   364   182   91
274   137   412   206   103   310   155   466   233   700
350   175   526   263   790   395   1186  593   1780  890
445   1336  668   334   167   502   251   754   377   1132
566   283   850   425   1276  638   319   958   479   1438
719   2158  1079  3238  1619  4858  2429  7288  3644  1822
911   2734  1367  4102  2051  6154  3077  9232  4616  2308
1154  577   1732  866   433   1300  650   325   976   488
244   122   61    184   92    46    23    70    35    106
53    160   80    40    20    10    5     16    8     4
2     1

The largest value was 9232.

```

Bonus #3
--------
For +30 bonus points, do both.


```
Starting number: 11
11    34    17    52    26    13    40    20    10    5
16    8     4     2     1

Terminated after 14 steps. The largest value was 52.

```

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)