import turtle

#now create a turtle object

trt = turtle.Turtle()

#create a screen

src=turtle.Screen()

#set the background color

src.bgcolor('black')

# 0 is the fastest speed

trt.speed(0)

#define the color to be used

colors=['red','green','orange','blue','purple','yellow']

#it has to be iterate same hexagonal designe so  use for loop

for i in range(300):

    #loop will iterate 300 times
    trt.pencolor(colors[i%6])
    trt.width(i/100 +1)
    #increase the width of the line in each iteration
    trt.forward(i)
    #as the value increase length of the benzene side also increase
    trt.left(59)
    #bend at  59 degree to form the angular design
    #its done
    #now hide the turtle after the design has been completed

trt.hideturtle()

#holding the screen after the completion of design

turtle.done()

