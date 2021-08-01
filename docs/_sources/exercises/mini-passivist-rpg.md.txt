# Mini Passivist RPG

It would be quite interesting if there were an RPG where your character refused to attack anything. Let's code it!

```eval_rst
* :download:`mini_passivist_rpg.py<examples/mini_passivist_rpg.py>`
```

Download the file and run it, it should output the following:

```
Enemy hits Awesome-Sauce for 22 damage.

Player: Awesome-Sauce
Health: 50
```

The problem is the player *starts* at `50` health, so we really didn't take any damage. 


What you should do
------------------
1. Modify the code to subtract the `damage_taken` value from the player's health stored in the dictionary.
2. Use the player's strength to apply some damage reduction to the ememy's attack. It's probably best not to subtract the whole strength value from the damage, perhaps a portion of it. More strength would have a greate effect at reducing incoming damage.
3. Create a loop that will continue this entire process of damaging and displaying the player's health until the player runs out of health. When the loop quits, print `"Game over"`. You should see something like:
    ```
    Enemy hits Awesome-Sauce for 13 damage.

    Player: Awesome-Sauce
    Health: 37

    Enemy hits Awesome-Sauce for 14 damage.

    Player: Awesome-Sauce
    Health: 23

    Enemy hits Awesome-Sauce for 12 damage.

    Player: Awesome-Sauce
    Health: 11

    Enemy hits Awesome-Sauce for 15 damage.

    Player: Awesome-Sauce
    Health: -4

    Game over
    ```

    
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)
