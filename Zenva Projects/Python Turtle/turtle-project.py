from turtle import *

#drawing a square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

#drawing a circle
circle(50) #arg represents radius in px
forward(100)
circle(50)

#changing color
color("#00CC00")
right(90)
forward(100)

#filling in shapes
begin_fill()
circle(50)
end_fill()

#changing background color
bgcolor("lightblue")

#lifting the pen
penup() #lifts pen so the trail does not follow the turtle
pendown() #puts the pen back down to continue drawing
done()