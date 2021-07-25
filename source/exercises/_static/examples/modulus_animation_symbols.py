import time
import os

repeats = 5
steps_per_second = 10

for i in range(11 * repeats):
    os.system("clear")

    if i % 11 == 0:
        print(" .oOo....... ")
    elif i % 11 == 1:
        print(" ..oOo...... ")
    elif i % 11 == 2:
        print(" ...oOo..... ")
    elif i % 11 == 3:
        print(" ....oOo.... ")
    elif i % 11 == 4:
        print(" .....oOo... ")
    elif i % 11 == 5:
        print(" ......oOo.. ")
    elif i % 11 == 6:
        print(" .......oOo. ")
    elif i % 11 == 7:
        print(" ........oOo ")
    elif i % 11 == 8:
        print(" o........oO ")
    elif i % 11 == 9:
        print(" Oo........o ")
    elif i % 11 == 10:
        print(" oOo........ ")

    time.sleep(1/steps_per_second)
