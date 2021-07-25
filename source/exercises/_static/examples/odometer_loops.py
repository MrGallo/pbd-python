import time


for thous in range(0, 10):
    for hund in range(0, 10):
        for tens in range(0, 10):
            for ones in range(0, 10):
                print("{}{}{}{}\r".format(thous, hund, tens, ones), end="")
                time.sleep(0.01)
