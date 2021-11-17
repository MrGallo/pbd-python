# Drain Method

Take this `Bathtub` class and add a `drain` method to it, so that when you send it an amount in liters (float) it will subtract that amount from the tub's `current_volume`. 

## Starter code

```python
class Bathtub:
    def __init__(self, color: str, current_volume: float) -> None:
        self.color = color
        self.current_volume = current_volume
    
    # add 'drain' method here


tub = Bathtub("white", 19.5)
tub.drain(10)
print(tub.current_volume)  # should be 9.5
```

---

©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>