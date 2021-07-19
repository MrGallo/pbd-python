# Variables and Names

Every serious computer program will deal with an awful lot of data and we need somewhere to store all that information. The computer will store your important data inside variables. Think of them as boxes (or containers) with a label on them (a name).

Because code can get quite long and complex, it is up to us to write code that not only works, but, code that is readable and understandable. We can help make our code readable by chosing descriptive variable names.

Have a look at the code below. See if you can guess what the output might be. To do this, I would start at the `print` functions and look up the data stored in the variables. You can have a look at the "What you should see" section to check if you guessed properly.

Type out the code below and get it to run. **Do not copy and paste**.

Name the file: `009_variables_and_names.py`

```python
team = "Toronto Blue Jays"
current_date = "July 18, 2021"
player = "Vladimir Guerrero Jr."
home_runs_to_date = 31
games_played = 88
total_season_games = 162
home_run_record = 73

games_remaining = total_season_games - games_played
home_runs_per_game = home_runs_to_date / games_played
projected_home_runs = home_runs_per_game * total_season_games
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {home_runs_per_game} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {projected_home_runs} home runs this season.")

```

What You Should See
-------------------
```
Vladimir Guerrero Jr. of the Toronto Blue Jays
currently has 31 home runs as of July 18, 2021.
The current MLB record for most home runs in a season is 73.
With 74 games remaining and an average of 0.3522727272727273 home runs per game,
it is False that he is on pace to break the record.
Vladimir Guerrero Jr. is projected to hit 57.06818181818182 home runs this season.
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will not receive any points.

1. Place a comment above each variable assignment explaining what is being calculated and what is being stored in the variable.
2. My code has two empty lines in it. Explain why I might have done this and explain how I chose to group specific lines of code.
3. Use the `round()` function to tidy up the *printing* of the values (not the values being stored in the variables).
4. Without knowing any of the values stored in the variables, how do you know the line `games_remaining = total_season_games - games_played` must be correct?

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)