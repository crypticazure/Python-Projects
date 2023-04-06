#Solar system project for Python Turtle
from turtle import *

#pseudocode for project management will be written in comments

#We will create a solar system using Python Turtle
#We will have a black background and different colored planets

bgcolor("black")

#creating the starting position for the turtle
penup()
backward(200)
right(90)
forward(200)
left(90)
pendown()

#creating the first planet
color("orange")
begin_fill()
circle(200)
end_fill()

#creating the starting position for second planet
penup()
forward(200)
pendown()

#repeat above process for each planet
color("grey")
begin_fill()
circle(20)
end_fill()

penup()
forward(150)
pendown()

#next planet
color("red")
begin_fill()
circle(100)
end_fill()

penup()
forward(200)
pendown()

color("green")
begin_fill()
circle(80)
end_fill()

done()