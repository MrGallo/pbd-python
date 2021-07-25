# Distance Formula

Write a function to compute the distance between two points. Given
two points `(x1, y1)` and `(x2, y2)`,the distance between these points is given by the formula:

![the distance formula](images/distance_formula.gif)

You must name the function `distance`, and it must return a `float` giving the distance between the two points.

Name your file `distance.py`

## Starter Code

```python
def main():
    # test the formula a bit
    d1 = distance(-2, 1, 1, 5)
    print(f"(-2,1) to (1,5) => {d1}")

    d2 = distance(-2, -3, -4, 4)
    print(f"(-2,-3) to (-4,4) => {d2}")

    print(f"(2,-3) to (-1,-2) => {distance(2, -3, -1, -2)}")

    print(f"(4,5) to (4,5) => {distance(4, 5, 4, 5)}" )


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    # put your code in here, remove "pass"
    pass


if __name__ == "__main__":
    main()
```

What you should see
-------------------

```
(-2,1) to (1,5) => 5.0
(-2,-3) to (-4,4) => 7.280109889280518
(2,-3) to (-1,-2) => 3.1622776601683795
(4,5) to (4,5) => 0.0
```
---


©2021 Daniel Gallo


This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)





Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)