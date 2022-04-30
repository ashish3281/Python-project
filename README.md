# Python-project
Turtle Programming in Python
Difficulty Level : Medium
Last Updated : 18 Oct, 2021
“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it! We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around. Commonly used turtle methods are :
 

Method	Parameter	Description
Turtle()	None	Creates and returns a new turtle object
forward()	amount	Moves the turtle forward by the specified amount
backward()	amount	Moves the turtle backward by the specified amount
right()	angle	Turns the turtle clockwise
left()	angle	Turns the turtle counterclockwise
penup()	None	Picks up the turtle’s Pen
pendown()	None	Puts down the turtle’s Pen
up()	None	Picks up the turtle’s Pen
down()	None	Puts down the turtle’s Pen
color()	Color name	Changes the color of the turtle’s pen
fillcolor()	Color name	Changes the color of the turtle will use to fill a polygon
heading()	None	Returns the current heading
position()	None	Returns the current position
goto()	x, y	Move the turtle to position x,y
begin_fill()	None	Remember the starting point for a filled polygon
end_fill()	None	Close the polygon and fill with the current fill color
dot()	None	Leave the dot at the current position
stamp()	None	Leaves an impression of a turtle shape at the current location
shape()	shapename	Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’
Plotting using Turtle

To make use of the turtle methods and functionalities, we need to import turtle.”turtle” comes packed with the standard Python package and need not be installed externally. The roadmap for executing a turtle program follows 4 steps:  

Import the turtle module
Create a turtle to control.
Draw around using the turtle methods.
Run turtle.done().
So as stated above, before we can use turtle, we need to import it. We import it as : 

from turtle import *
# or
import turtle
After importing the turtle library and making all the turtle functionalities available to us, we need to create a new drawing board(window) and a turtle. Let’s call the window as wn and the turtle as skk. So we code as: 

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
Now that we have created the window and the turtle, we need to move the turtle. To move forward 100 pixels in the direction skk is facing, we code: 

skk.forward(100)
We have moved skk 100 pixels forward, Awesome! Now we complete the program with the done() function and We’re done! 

turtle.done()
So, we have created a program that draws a line 100 pixels long. We can draw various shapes and fill different colors using turtle methods. There’s plethora of functions and programs to be coded using the turtle library in python. Let’s learn to draw some of the basic shapes. 
