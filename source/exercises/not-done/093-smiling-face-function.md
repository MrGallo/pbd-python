# Smiling Face Function


Write a function that displays a smiling face at a certain place
on the screen. The function must be named as below, and it *must*
be able to display the face anywhere on the screen specified by the parameters
`x` and `y`. You may borrow code from previous assignments
if you want, although it is probably better if the face is relatively small so
you have room to draw several of them on the screen at once.


Then, inside the `paint()` method, call the function a few times to draw
several faces on the screen.


## Files Needed


* [SmilingFaceFunction.java](examples/SmilingFaceFunction.java)



```
import java.awt.*;
import javax.swing.JFrame;

public class SmilingFaceFunction extends Canvas
{
    public void paint( Graphics g )
    {
        drawSmilingFace(g,100,100);
        drawSmilingFace(g,400,350);
        // etc
    }

    public void drawSmilingFace( Graphics g, int x, int y )
    {
        // Draws a smiling face on the screen, where the point (x,y) is
        //  the upper-left corner of a box containing the face.

        // draw circle for the head

        // draw eyes

        // draw mouth
    }

    public static void main(String[] args)
    {
        // You can change the title or size here if you want.
        JFrame win = new JFrame("Smiling Face Function");
        win.setSize(1024,768);
        win.setDefaultCloseOperation(JFrame.EXIT\_ON\_CLOSE);
        win.add( new SmilingFaceFunction() );
        win.setVisible(true);
    }

}

```


```



```



---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)