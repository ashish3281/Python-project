# Python-project
<h1>Turtle Programming in Python</h1>
<hr>
<p>“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it! We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around. Commonly used turtle methods are :</p>
 <br>

<h3>Method	Parameter	Description</h3>
<br>
<pre>
Turtle()	None	Creates and returns a new turtle object<br>
forward()	amount	Moves the turtle forward by the specified amount<br>
backward()	amount	Moves the turtle backward by the specified amount<br>
right()	angle	Turns the turtle clockwise<br>
left()	angle	Turns the turtle counterclockwise<br>
penup()	None	Picks up the turtle’s Pen<br>
pendown()	None	Puts down the turtle’s Pen<br>
up()	None	Picks up the turtle’s Pen<br>
down()	None	Puts down the turtle’s Pen<br>
color()	Color name	Changes the color of the turtle’s pen<br>
fillcolor()	Color name	Changes the color of the turtle will use to fill a polygon<br>
heading()	None	Returns the current heading<br>
position()	None	Returns the current position<br>
goto()	x, y	Move the turtle to position x,y<br>
begin_fill()	None	Remember the starting point for a filled polygon<br>
end_fill()	None	Close the polygon and fill with the current fill color<br>
dot()	None	Leave the dot at the current position<br>
stamp()	None	Leaves an impression of a turtle shape at the current location<br>
shape()	shapename	Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’<br>
</pre>
<hr>
<h3>Plotting using Turtle</h3>
<br>
<p>To make use of the turtle methods and functionalities, we need to import turtle.”turtle” comes packed with the standard Python package and need not be installed externally. The roadmap for executing a turtle program follows 4 steps:  
</p><br>
1) Import the turtle module<br>
2) Create a turtle to control.<br>
3) Draw around using the turtle methods.<br>
4) Run turtle.done().<br>
<hr>
<h3>Example></h3>
<br>

from turtle import *<br>
import turtle<br>
<p>After importing the turtle library and making all the turtle functionalities available to us, we need to create a new drawing board(window) and a turtle. Let’s call the window as wn and the turtle as skk. So we code as: <p><br>
<pre>
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
Now that we have created the window and the turtle, we need to move the turtle. To move forward 100 pixels in the direction skk is facing, we code: 

skk.forward(100)
We have moved skk 100 pixels forward, Awesome! Now we complete the program with the done() function and We’re done! 

turtle.done()
</pre>
<p>So, we have created a program that draws a line 100 pixels long. We can draw various shapes and fill different colors using turtle methods. There’s plethora of functions and programs to be coded using the turtle library in python. </p>
<hr>
<h2>OUTPUTS</h2>
