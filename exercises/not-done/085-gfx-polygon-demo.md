# Polygon Demo


Here are some more examples of the various functions at your disposal
in Java's graphics library. Download the following code and get it to
compile.


## Files Needed


* [PolygonDemo.java](examples/PolygonDemo.java)



```
**import** java.awt.*;
**import** javax.swing.JFrame;
**import** java.awt.Polygon;

**public class** PolygonDemo **extends** Canvas
**{**
    **public void** paint**(** **Graphics** g **)**
    **{**
        g.setColor**(**Color.black**)**;
        g.draw**String****(****"Hey, a triangle!"**, 50, 50**)**;
        
        Polygon tri = **new** Polygon**()**;
        tri.addPoint**(**100, 100**)**;
        tri.addPoint**(**100, 300**)**;
        tri.addPoint**(**200, 300**)**;
        
        g.setColor**(**Color.blue**)**;
        g.fillPolygon**(**tri**)**;
        
        Polygon pent = **new** Polygon**()**;
        pent.addPoint**(**450, 200**)**;
        pent.addPoint**(**500, 250**)**;
        pent.addPoint**(**475, 350**)**;
        pent.addPoint**(**425, 350**)**;
        pent.addPoint**(**400, 250**)**;
        
        g.setColor**(**Color.green**)**;
        g.fillPolygon**(**pent**)**;

        Polygon hex = **new** Polygon**()**;
                
        **// use trig to make a regular hexagon**
        **int** radius = 100; **// pixels**
        **int** xCenter = 200;
        **int** yCenter = 500;
        **for** **(** **double** ang = 0; ang<2***Math**.PI; ang=ang+**(**2***Math**.PI**)**/6.0**)**
        **{**
            **double** xDelta = radius * **Math**.cos**(**ang**)**;
            **double** yDelta = -radius * **Math**.sin**(**ang**)**;
            hex.addPoint**(**xCenter+**(****int****)**xDelta, yCenter+**(****int****)**yDelta**)**;
        **}**

        g.setColor**(**Color.black**)**;
        g.fillPolygon**(**hex**)**;
    **}**

    **public static void** main**(****String****[]** args**)**
    **{**
        JFrame win = **new** JFrame**(****"Polygon Demo"****)**;
        win.setSize**(**1024,768**)**;
        win.setDefaultCloseOperation**(**JFrame.EXIT\_ON\_CLOSE**)**;
        win.add**(** **new** PolygonDemo**()** **)**;
        win.setVisible**(****true****)**;
    **}**

**}**

```

What You Should Do on Your Own
------------------------------


Assignments turned in *without* these things will receive
half credit or less.


1. There is a green pentagon being drawn on the screen. What happens
 if you change the order of the points being added? Answer in a comment.

 - Make a [trapezoid](https://en.wikipedia.org/wiki/Trapezoid)
 somewhere on the screen. The color doesn't matter, and it doesn't matter
 if it's filled-in or an outline.




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