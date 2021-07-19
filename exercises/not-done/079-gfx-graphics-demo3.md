# Graphics Demo 3


Here are some more examples of the various functions at your disposal
in Java's graphics library. Type in the following code and get it to
compile.


## Files Needed


* [GraphicsDemo3.java](examples/GraphicsDemo3.java)



```
**import** java.awt.*;
**import** javax.swing.JFrame;

**public** **class** GraphicsDemo3 **extends** Canvas
**{**
    **public** **void** paint**(** **Graphics** g **)**
    **{**
        **// lines**
        g.setColor**(**Color.green**)**;
        g.drawLine**(**10,100,400,100**)**;
        g.setColor**(**Color.blue**)**;
        g.drawLine**(**50,150,100,180**)**;
        g.setColor**(**Color.magenta**)**;
        g.drawLine**(**100,350,300,230**)**;

        g.setColor**(**Color.black**)**;

        **// fonts**
        g.draw**String****(****"**Graphics** are pretty neat."**, 500, 100**)**;
        g.setFont**(****new** Font**(****"Consolas"**, Font.PLAIN, 36**)****)**; **// 36-pt plain**
        g.draw**String****(****"Yes, they are."**, 400, 200**)**;

        g.setColor**(**Color.white**)**;
        g.setFont**(****new** Font**(****"Calibri"**, Font.BOLD+Font.ITALIC, 60**)****)**; **// 60-pt italic bold**
        g.draw**String****(****"Leander Lions"**, 300, 350**)**;

        g.setColor**(**Color.blue**)**;
        g.setFont**(**Font.decode**(****"Calibri-BOLDITALIC-60"****)****)**; **// a different way to specify the same font**
        g.draw**String****(****"Leander Lions"**, 290, 360**)**;
        
        g.setColor**(**Color.black**)**;
        g.setFont**(****new** Font**(**null**)****)**; **// restore default font**

        **int** x=400, y=490;
        g.drawRect**(**x,y,150,20**)**;
        g.draw**String****(****"Where is the starting point?"**, x,y**)**;
        g.setColor**(**Color.red**)**;
        g.drawLine**(**x,y,x,y**)**;	**// drawing a line from a point to itself makes a 1px-by-1px dot**

    **}**

    **public** **static** **void** main**(** **String****[]** args **)**
    **{**
        JFrame win = **new** JFrame**(****"GraphicsDemo3: Fonts and Lines"****)**;
        win.setSize**(**800,600**)**;
        win.setDefaultCloseOperation**(**JFrame.EXIT\_ON\_CLOSE**)**;
        GraphicsDemo3 canvas = **new** GraphicsDemo3**(****)**;
        win.add**(** canvas **)**;
        win.setVisible**(****true****)**;
    **}**
**}**

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
half credit or less. Answer any questions in comments at the top of
`GraphicsDemo3.java`.


1. When drawing a line, what do the four numbers represent?
 - Make a short red line that intersects the long green line.
 - Make a short red line that is roughly perpendicular to the diagonal "magenta" line.
 - When drawing a rectangle, where on the rectangle is the starting point you provide?
 Use the key below.


```
  the upper-left corner? - o......     ......o - the upper-right corner?
                           .......     .......
                           .......     .......

                           .......     .......
                           .......     .......
  the lower-left corner? - o......     ....... - the lower-right corner?

---------------------------------------------------------------------------------

                                 ...o... - the top of the center line?
                                 .......
                                 .......

                           .......     .......
middle of the left side? - o......     ......o - middle of the right side?
                           .......     .......

                                 .......
                                 .......
                                 ...o... - the bottom of the center line?

---------------------------------------------------------------------------------

                                 .......
                or, the absolute ...o... center of the rectangle?
                                 .......

```
- When drawing strings, where on the string is the starting point you provide?
 - When setting a custom font, what happens if you provide a font that doesn't exist?
 - When setting a custom font, what happens if you provide a font that isn't installed on this machine?
 - Change the first "Leander Lions" (the white one) to a different font.
 Change the blue "Leander Lions" to match it.










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