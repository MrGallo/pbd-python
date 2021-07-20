# Magic 8-Ball

## Starter Code
Name your file: `042_magic_8ball.py`
```python
import random


choice = random.randrange(1, 16)  # 1-15
response = ""

if choice == 1:
    response = "It is certain"
elif choice == 2:
    response = "It is decidedly so"
elif choice == 3:
    response = "Without a doubt"
elif choice == 4:
    response = "Yes - definitely"
elif choice == 5:
    response = "You may rely on it"
elif choice == 6:
    response = "As I see it, yes"
elif choice == 7:
    response = "Most likely"
elif choice == 8:
    response = "Outlook good"
elif choice == 9:
    response = "Signs point to yes"
elif choice == 10:
    response = "Yes"
elif choice == 11:
    response = "Reply hazy, try again"
elif choice == 12:
    response = "Ask again later"
elif choice == 13:
    response = "Better not tell you now"
elif choice == 14:
    response = "Cannot predict now"
elif choice == 15:
    response = "Concentrate and ask again"
else:
    response = "8-BALL ERROR!"

print("MAGIC 8-BALL SAYS: " + response)

```

What You Should See
-------------------
Your answers will probably be different than these. Actually, that's kind of the point.
```
MAGIC 8-BALL SAYS: It is decidedly so

```

```
MAGIC 8-BALL SAYS: Reply hazy, try again

```

```
MAGIC 8-BALL SAYS: Signs point to yes

```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive
no credit.

1. The real Magic 8-Ball™ contains `20` responses, not `15`. Change the code so that it picks a random
 number from `1-20`, and add the following five responses:
	* `"Don't count on it"`
	* `"My reply is no"`
	* `"My sources say no"`
	* `"Outlook not so good"`
	* `"Very doubtful"`
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)


Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)