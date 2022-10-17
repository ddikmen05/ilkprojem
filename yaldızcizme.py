import turtle
from turtle import *
from random import randint

# Page setup
# Setup(1000, 800)
speed(5)
bgcolor("pink")

# Function to draw one star
def star():
    begin_fill()
    width(200)
    for i in range(5):
        forward(600)
        right(144)
        end_fill()
    end_fill()

        for i in range(20):
            x = randint(-400, 400)
            y = randint(-250, 250)
            star()
            penup()
            goto(x, y)
            pendown()

star()
done()

