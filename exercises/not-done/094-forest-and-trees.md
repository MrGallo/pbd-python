# Forest and Trees


For this assignment, you need to write two functions.



`public void drawTree( Graphics g, int x, int y )`
this functions must draw a tree on the screen. Use a brownish rectangle
 for the trunk, and a green triangle (using `fillPolygon()`)
 for the branches. You should make it so that `x` is the left-most
 part of the branches, and `y` is the tallest part of the tree.
 You should make each tree relatively small.
`public void drawForest( Graphics g, int x, int y, int w, int h )`
this functions should call the `drawTree()` method inside a loop in
 order to draw many trees within a certain region on the screen. The positions
 of the trees within the forest should be random, but no part of any tree should extend
 past the boundaries given.

Once you're done, things should look something like this:

 ForestAndTrees


## Files Needed


* [ForestAndTrees.java](examples/ForestAndTrees.java)




|  |  |
| --- | --- |
| ![tree with various points labeled](examples/tree_big_annotated.png) The diagram to the left is not to scale.  

 A tree with a width of 50 and a height of 100 looks like this:
 ![tree](examples/tree_small.png) | |



```



```



---


©2013–2015 Graham Mitchell


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)




