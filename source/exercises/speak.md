# Speak

Create the class with the following UML. We will be giving the ``Animal`` class an instance method called ``speak``. The purpose is to simply print out the string ``"GENERIC ANIMAL SOUND"``.

![Student UML](examples/uml-animal-speak.png)

## Starter code
```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    # place the instance method here (in the class)


a = Animal("dog")

a.speak()  # will raise an AttributeError
           # unless you implement it in the class
```

---

©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>