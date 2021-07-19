# Interpreter Check

This assignment is designed to make sure that the Python interpreter is correctly installed on your machine.

Open a terminal window or command prompt. 

Windows
-------
Use the search bar to find "Command Prompt" or "cmd" or "Powershell" and run the program. Alternatively you can hit `WindowsKey + R` and type `cmd` and click "ok".

Mac
---
Click the Launchpad icon in the Dock, type `Terminal` in the search field, then click Terminal. Or, in the Finder, open the `/Applications/Utilities` folder, then double-click Terminal.

 Article: *[Open or quit Terminal on Mac](https://support.apple.com/en-ca/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)*.

Test it out
-----------
Next, type the `python --version` command in your terminal.

```
Microsoft Windows [Version 10.0.19043.1110]
(c) Microsoft Corporation. All rights reserved. 

C:\>python --version
```

You will see one of two things. 

1. If the Python interpreter *is* correctly installed, you should see a version number like so:
    ```
    C:\>python --version
    Python 3.9.5
    ```
    The exact version number doesn't matter, as long as it starts with `3.x.x`.

2. If the Python interpreter is *not* correctly installed, then you'll see an error like so:
    ```
    C:\>python --version
    'python' is not recognized as an internal or external command, operable program or batch file.
    ```
    The most common reason for this is when you installed Python you **did not check the `Add Python 3.x to PATH` option**. Please rewatch the [installation video](https://youtu.be/YYXdXT2l-Gg?t=427) and pay careful attention at the `7:06` mark.

    If that doesn't help, please rewatch the whole video and pay careful attention to each step Corey walks through.

If you do have to re-install Python, you must close down the terminal for the changes to take effect. Open the command prompt once again and try to check the Python version once more:

```
Microsoft Windows [Version 10.0.19043.1110]
(c) Microsoft Corporation. All rights reserved. 

C:\>python --version
Python 3.9.5
```

Success!

---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)