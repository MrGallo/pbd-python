# Graphics Demo 1


GRAPHICS! Kids, we're going to learn how to draw some stuff on the
screen in a Java application. Download the following code
file and get it to compile.


## Files Needed


* [GraphicsDemo1.java](examples/GraphicsDemo1.java)



```
**import** java.awt.*;
**import** javax.swing.JFrame;

**public** **class** **Graphics**Demo1 **extends** Canvas
**{**
    **public** **void** paint**(** **Graphics** g **)**
    **{**
        g.setColor**(**Color.green**)**;
        g.drawRect**(**50,20,100,200**)**;  **// draw a rectangle**
        g.fillOval**(**160,20,100,200**)**; **// draw a filled-in oval**
        g.setColor**(**Color.blue**)**;
        g.fillRect**(**200,400,200,20**)**; **// a filled-in rectangle**
        g.drawOval**(**200,430,200,100**)**;
        
        g.setColor**(**Color.black**)**;
        g.drawString**(****"Graphics are pretty neat."**, 500, 100**)**;
        **int** x = getWidth**(****)** / 2;
        **int** y = getHeight**(****)** / 2;
        g.drawString**(****"The first letter of this string is at **(**"** + x + **","** + y + **"**)**"**, x, y**)**;
    **}**

    **public** **static** **void** main**(** **String****[]** args **)**
    **{**
        **// You can change the title or size here **if** you want.**
        JFrame win = **new** JFrame**(****"**Graphics**Demo1"****)**;
        win.setSize**(**800,600**)**;
        win.setDefaultCloseOperation**(**JFrame.EXIT\_ON\_CLOSE**)**;
        GraphicsDemo1 canvas = **new** GraphicsDemo1**()**;
        win.add**(** canvas **)**;
        win.setVisible**(**true**)**;
    **}**
**}**

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
half credit or less. Answer any questions in comments at the top of
`GraphicsDemo1.java`.


1. How big is the window that appears? How many pixels wide? How many pixels tall?
 - In the call to the function `g.drawRect()`, there are four numbers. What
 do they mean? Try changing them to figure it out.
 - What about the call to `fillOval()`? What do the four numbers mean here?
 - What are the two numbers in the call to `drawString()`?
 - What happens when two objects overlap? Which one is drawn on top?
 - Add a red, filled-in square somewhere in the lower-right of the canvas.








```



```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)