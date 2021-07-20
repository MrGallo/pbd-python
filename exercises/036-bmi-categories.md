# BMI Categories

The body mass index (BMI) is commonly used by health and nutrition professionals to estimate human body fat in populations. It is computed by taking the individual's weight (mass) in kilograms and dividing it by the square of their height in meters.

Start with the [BMI Calculator](020-bmi-calculator.md) you
wrote previously (`020_bmi_calculator.py`). Then use some `if`
statements to show the category for a given BMI.


| BMI | category |
| - | - |
| less than `18.5` | underweight |
| `18.5` to `24.9` | normal weight |
| `25.0` to `29.9` | overweight |
| `30.0` or more | obese |

Name the file: `036_bmi_categories.py`


*Note*: The formula doesn't work well for athletes with a lot of muscle, or people who are extremely short or very tall (quite unreliable). If you are concerned about your BMI, check with your doctor.


Sample Output
-------------
```
Your height in m: 1.75
Your weight in kg: 73

Your BMI is 23.83673
BMI Category: normal weight

```

It doesn't matter whether you input the values in metric (kilos and meters)
or Imperial measurements (feet/inches and pounds).

```
Your height in inches: 69
Your weight in pounds: 220

Your BMI is 32.5
BMI Category: obese

```

Bonus #1 - More Categories
--------------------------

For +10 bonus points, use more `if` statements
to show the ALL the BMI categories.

| BMI | category |
| - | - |
| less than 15.0 | very severely underweight |
| 15.0 to 16.0 | severely underweight  |
| 16.1 to 18.4 | underweight |
| 18.5 to 24.9 | normal weight |
| 25.0 to 29.9 | overweight |
| 30.0 to 34.9 | moderately obese |
| 35.0 to 39.9 | severely obese |
| 40.0 and up | very severely (or "morbidly") obese |


```
Your height in inches: 70
Your weight in pounds: 90

Your BMI is 12.9
BMI Category: very severely underweight

```

---

©2021 Daniel Gallo

This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)