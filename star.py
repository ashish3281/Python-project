import turtle

star = turtle.Screen()
star.bgcolor("blue")
t = turtle.Turtle()

size=80
t.color("white")
t.width(4)
angle= 120
t.fillcolor("white")
t.begin_fill()
for side in range(5):
    t.forward(size)
    t.right(angle)
    t.forward(size)
    t.right(72 - angle)
t.end_fill()
