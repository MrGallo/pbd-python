# If Intro

Here is the next Python program you'll enter, which introduces you to the if statement. Type this in, make it run
exactly right and then we'll see if your practice has paid off.

Name your file:

`if_intro.py`

```
robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
```

What You Should See
-------------------
```
Almost at the ball
You are beyond the goal.
Moing forward 5
At the ball
Picking up the ball.
Now make your way to the goal.
Moing back 15
You reached the goal and scored!
```

What You Should Do on Your Own
------------------------------
Assignments turned in *without* these things will receive half credit or less.

In this section, you're going to try to guess what you think the if statement is and what it does.

1. What do you think the if does to the code under it? Put your answer in a comment in the code.
2. What is the purpose indenting in the if statement? How can we tell what code is enclosed in an if branch and what code is not? Answer in a comment.
3. Change the initial locations of the objects and get the program to output the same thing.
4. What do the operators `+=` and `-=` do?

---

©2021 Daniel Gallo

This assignment is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License](https://creativecommons.org/licenses/by-nc-sa/3.0/us/deed.en_US).  

![Creative Commons License](images/by-nc-sa.png)

Adapted for Python from Graham Mitchell's [Programming By Doing](https://programmingbydoing.com/)