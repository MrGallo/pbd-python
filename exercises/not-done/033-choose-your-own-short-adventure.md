# Choose Your Own Adventure!


Make a short "Choose Your Own Adventure" game. The starting room
should give the user two choices. Then the second room they travel
to should give them two more choices. Finally the third room should
give them two choices.


This means your game will have eight possible "endings". Your game
will also have a total of fifteen rooms:



```
        \_ R1 \_
       /      \
    R2          R3
   /  \        /  \
 R4    R5    R6    R7
 /\    /\    /\    /\
E1 E2 E3 E4 E5 E6 E7 E8

```

You must use *nested* `if`
statements to do this.



```
WELCOME TO MITCHELL'S TINY ADVENTURE!

You are in a creepy house!  Would you like to go "upstairs" or into the
"kitchen"?
> kitchen

There is a long countertop with dirty dishes everywhere.  Off to one side
there is, as you'd expect, a refrigerator. You may open the "refrigerator"
or look in a "cabinet".
> refrigerator

Inside the refrigerator you see food and stuff.  It looks pretty nasty.
Would you like to eat some of the food? ("yes" or "no")
> no

You die of starvation... eventually.

```

 



```
WELCOME TO MITCHELL'S TINY ADVENTURE!

You are in a creepy house!  Would you like to go "upstairs" or into the
"kitchen"?
> upstairs

Upstairs you see a hallway.  At the end of the hallway is the master
"bedroom".  There is also a "bathroom" off the hallway.  Where would you like
to go?
> bedroom

You are in a plush bedroom, with expensive-looking hardwood furniture.  The
bed is unmade.  In the back of the room, the closet door is ajar.  Would you
like to open the door? ("yes" or "no")
> no

Well, then I guess you'll never know what was in there.  Thanks for playing,
I'm tired of making nested if statements.

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)