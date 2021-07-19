# Graphics Demo 2: Arcs and Custom Colors


Here are some more examples of the various functions at your disposal
in Java's graphics library. Type in the following code and get it to
compile.


## Files Needed


* [GraphicsDemo2.java](examples/GraphicsDemo2.java)



```
**import** java.awt.*;
**import** javax.swing.JFrame;

**public** **class** GraphicsDemo2 **extends** Canvas
**{**
    **public** **void** paint**(** **Graphics** g **)**
    **{**
        g.setColor**(**Color.black**)**;

        g.drawRect**(**50,20,100,200**)**;  **// draw a rectangle**
        g.drawOval**(**160,20,100,200**)**; **// draw a filled-in oval**

        **//arcs**
        g.drawArc**(**270,20,100,200,0,270**)**; **// draw an arc that starts at 0 degrees**
                                         **// and has an arclength of 270 degrees**
        g.drawArc**(**50,250,150,150,90,180**)**;
        g.drawArc**(**210,250,150,150,45,90**)**;
        g.fillArc**(**210,280,150,150,45,90**)**;

        g.setColor**(**Color.yellow**)**;
        g.fillArc**(**150,400,150,150,45,270**)**; **// chomp**
        
        **// custom colors**
        Color myOrange = **new** Color**(**230,92,0**)**; **// amount of red, green, blue in the color**
                                              **// Each component has a value from 0-255**
        g.setColor**(**myOrange**)**;
        g.fillOval**(**500,50,150,150**)**;

        Color myGrey = **new** Color**(**238,238,238**)**;
        g.setColor**(**myGrey**)**;
        g.fillOval**(**550,100,50,50**)**;

        g.setColor**(**Color.yellow**)**;
        g.fillOval**(**500,210,150,150**)**;

        g.setColor**(**Color.green**)**;
        g.fillOval**(**500,370,150,150**)**;
    **}**

    **public** **static** **void** main**(** **String****[]** args **)**
    **{**
        JFrame win = **new** JFrame**(****"GraphicsDemo2: Arcs and Colors"****)**;
        win.setSize**(**800,600**)**;
        win.setDefaultCloseOperation**(**JFrame.EXIT\_ON\_CLOSE**)**;
        GraphicsDemo2 canvas = **new** GraphicsDemo2**(****)**;
        win.add**(** canvas **)**;
        win.setVisible**(****true****)**;
    **}**
**}**

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
half credit or less.


1. Using either the [Color Schemer Online](http://www.colorschemer.com/online.html)
 or [ColorPicker.com](http://www.colorpicker.com/), make a color of your
 own and change the middle circle (the yellow one) to your custom color.

 - Draw a second, slightly smaller pacman to the right of the
 first pacman. Make her face to the left and make her pink.




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