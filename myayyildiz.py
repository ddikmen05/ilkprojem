import turtle
from turtle import *


bgcolor("red")
color("white")
def star():
    fillcolor("white")
    begin_fill()
    width(1)
    for i in range(5):
        forward(100)
        left(72)
        forward(100)
        right(144)

    end_fill()
    penup()
    goto(-250,-200)
    pendown()
    begin_fill()
    circle(200)
    end_fill()
    penup()
    fillcolor("red")
    color("red")
    goto(-175, -175)
    pendown()
    begin_fill()
    circle(165)
    end_fill()


star()
done()
