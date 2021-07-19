# do-while Swimming


So far you have only worked with one type of loop: the `while`
loop. But there is another type: the "do-while" loop.


The do-while loop works *almost* exactly like a
`while` loop. In fact, most of the time they
are equivalent. Examine the program below to see if you can figure
out the tiny difference.


## Files Needed


* [DoWhileSwimming.java](examples/DoWhileSwimming.java)



```
**import** java.util.**Scanner**;

**public** **class** DoWhileSwimming
**{**
    **public static void** main**(** **String****[]** args **)** throws **Exception**
    **{**
        **Scanner** keyboard = **new** **Scanner****(****System**.in**)**;

        **String** swimmer1 = **"GALLANT"**;
        **String** swimmer2 = **"GOOFUS "**;

        **double** minimumTemperature = 79.0; **// degrees Fahrenheit**
        **double** currentTemperature;
        **double** savedTemperature;
        **int** swimTime;

        **System**.out.print**(****"What is the current water temperature? "****)**;
        currentTemperature = keyboard.next**Double******(****)****;
        savedTemperature = currentTemperature; **// saves a copy of this value so we can get it back later.**

        **System**.out.println**(** **"\nOkay, so the current water temperature is "** + currentTemperature + **"F."** **)**;
        **System**.out.println**(** swimmer1 + **" approaches the lake...."** **)**;

        swimTime = 0;
        **while** **(** currentTemperature >= minimumTemperature **)**
        **{**
            **System**.out.print**(** **"\t"** + swimmer1 + **" swims **for** a bit."** **)**;
            swimTime++;
            **System**.out.println**(** **" Swim time: "** + swimTime + **" min."** **)**;
            Thread.sleep**(**600**)**; **// pauses for 600 milliseconds**
            currentTemperature -= 0.5; **// subtracts 1/2 a degree from the water temperature**
            **System**.out.println**(** **"\tThe current water temperature is now "** + currentTemperature + **"F."** **)**;
        **}**

        **System**.out.println**(** swimmer1 + **" stops swimming. Total swim time: "** + swimTime + **" min."** **)**;

        currentTemperature = savedTemperature; **// restores original water temperature**

        **System**.out.println**(** **"\nOkay, so the current water temperature is "** + currentTemperature + **"F."** **)**;
        **System**.out.println**(** swimmer2 + **" approaches the lake...."** **)**;

        swimTime = 0;
        **do**
        **{**
            **System**.out.print**(** **"\t"** + swimmer2 + **" swims **for** a bit."** **)**;
            swimTime++;
            **System**.out.println**(** **" Swim time: "** + swimTime + **" min."** **)**;
            Thread.sleep**(**600**)**;
            currentTemperature -= 0.5;
            **System**.out.println**(** **"\tThe current water temperature is now "** + currentTemperature + **"F."** **)**;

        **}** **while** **(** currentTemperature >= minimumTemperature **)**;

        **System**.out.println**(** swimmer2 + **" stops swimming. Total swim time: "** + swimTime + **" min."** **)**;
    **}**
**}**

```

What You Should See
-------------------


Goofus and Gallant are both going swimming. They hate to swim in cold water;
once the water temperature drops below 79°F, they stop.


Run the program, and type in 80.5 for the water temperature.



```
What is the current water temperature? 80.5

Okay, so the current water temperature is 80.5F.
GALLANT approaches the lake....
        GALLANT swims for a bit. Swim time: 1 min.
        The current water temperature is now 80.0F.
        GALLANT swims for a bit. Swim time: 2 min.
        The current water temperature is now 79.5F.
        GALLANT swims for a bit. Swim time: 3 min.
        The current water temperature is now 79.0F.
        GALLANT swims for a bit. Swim time: 4 min.
        The current water temperature is now 78.5F.
GALLANT stops swimming. Total swim time: 4 min.

Okay, so the current water temperature is 80.5F.
GOOFUS  approaches the lake....
        GOOFUS  swims for a bit. Swim time: 1 min.
        The current water temperature is now 80.0F.
        GOOFUS  swims for a bit. Swim time: 2 min.
        The current water temperature is now 79.5F.
        GOOFUS  swims for a bit. Swim time: 3 min.
        The current water temperature is now 79.0F.
        GOOFUS  swims for a bit. Swim time: 4 min.
        The current water temperature is now 78.5F.
GOOFUS  stops swimming. Total swim time: 4 min.

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
no credit.


1. Run the program, and type in 80.5 for the current
 water temperature. Do Goofus and Gallant swim for the same amount of
 time? Put your answer in a comment.

 - Run the program again, but this time enter 78 for
 the starting temperature. What changes?

 - Does Gallant check the water temperature first, or does he
 just dive right in?

 - What about Goofus? Does he check the water temperature first
 or just dive in?

 - What is the difference between a `while`
 loop and a "do-while" loop?

 - One of these loops is sometimes called a "pre-test loop",
 and the other is called a "post-test loop". Which one is which?








```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)