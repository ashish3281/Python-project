import turtle


pattern = turtle.Screen()
turtle.speed(0)
pattern.bgcolor('black')
colors=['red','green','blue','purple']

for i in range(100):
    turtle.pencolor(colors[i%4])
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.hideturtle()

turtle.done
