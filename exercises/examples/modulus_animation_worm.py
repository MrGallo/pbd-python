import time
import os


for i in range(80):
    os.system("clear")
    
    if i % 16 == 0:
        print(" ********                 ")
    elif i % 16 == 1:
        print("   ********               ")
    elif i % 16 == 2:
        print("     ********             ")
    elif i % 16 == 3:
        print("       ********           ")
    elif i % 16 == 4:
        print("         ********         ")
    elif i % 16 == 5:
        print("           ********       ")
    elif i % 16 == 6:
        print("             ********     ")
    elif i % 16 == 7:
        print("               ********   ")
    elif i % 16 == 8:
        print("                 ******** ")
    elif i % 16 == 9:
        print("               ********   ")
    elif i % 16 == 10:
        print("             ********     ")
    elif i % 16 == 11:
        print("           ********       ")
    elif i % 16 == 12:
        print("         ********         ")
    elif i % 16 == 13:
        print("       ********           ")
    elif i % 16 == 14:
        print("     ********             ")
    elif i % 16 == 15:
        print("   ********               ")
    
    time.sleep(0.1)
    
