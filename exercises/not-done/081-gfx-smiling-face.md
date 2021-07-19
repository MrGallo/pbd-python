# A Smiling Face


Make a graphics program that displays a "smiley face" on
the screen. The circle must be yellow. There must be a curve
of a smile in the lower part of the face, and two small circles
for eyes in the upper part of the face. The "mouth" should be
red and the eyes should be blue.


Here is a working example version:

 SmilingFace


If you'd like a grid to help line things up, then paste the
following code at the end of your own code (inside 
`public void` `paint()`).



```
**// labels**
g.setColor**(**Color.black**)**;
g.setFont**(****new** Font**(**null**))**;
**for** **(** **int** X=0; X<800; X += 50 **)**
    g.draw**String****(** **String**.valueOf**(**X**)**, X, 50 **)**;
**for** **(** **int** Y=100; Y<600; Y += 50 **)**
    g.draw**String****(** **String**.valueOf**(**Y**)**, 28, Y **)**;
**// lines**
g.setColor**(**Color.lightGray**)**;
**for** **(** **int** X=0; X<800; X += 50 **)**
    g.drawLine**(**X,0,X,599**)**;    **// horizontal**
**for** **(** **int** Y=0; Y<600; Y += 50 **)**
    g.drawLine**(**0,Y,799,Y**)**;    **// vertical**

```


```



```



---


©2013–2015 Graham Mitchell


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)




