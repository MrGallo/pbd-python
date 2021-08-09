# Try a Validation Loop

Run this starter code. Pretty simple.

```python
def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except _____Error:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()
```

## What you should do
1. What is the error that happens when you try to convert a string that cannot be converted to an integer?
2. Use that error in the `except` section.
3. Purposefully enter invalid input to see how the program handles the error.
4. Why doesn't the loop `break` right after taking the input?


## What it should look like
```
Please enter your age: hello there sonny!
Need to input an integer!

Please enter your age: hmm? could you speak in my good ear?
Need to input an integer!

Please enter your age: oh, sorry..
Need to input an integer!

Please enter your age: 105
Wow, you are 105 years old.
```

---


©2021 Daniel Gallo

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>