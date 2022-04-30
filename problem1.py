import turtle

canvas = turtle.Screen()
canvas.bgcolor("light green")
canvas.title("my first drawing")

tur = turtle.Turtle()
tur.shape("turtle")
tur.speed(1)
#square shape
#tur.forward(200)
#tur.right(90)
#tur.forward(200)
#tur.right(90)
#tur.forward(200)
#tur.right(90)
#tur.forward(200)


#any sided shape
def makeShape(numSides):
    for i in range(numSides):
        
        tur.forward(100)
        tur.left(360.0/numSides)
