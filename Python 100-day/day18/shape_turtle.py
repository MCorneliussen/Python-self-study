from turtle import Turtle, Screen
from random import choice

colors = ["blue", "yellow", "green", "pink", "orange", "black", "gray", "purple", "aquamarine"]



johnny = Turtle()
johnny.shape("turtle")
johnny.color("black", "darkgreen")


def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        johnny.forward(50)
        johnny.right(angle)
        
num_side = 3

while not num_side == 13:
    draw_shape(num_side)
    num_side += 1
    new_color = choice(colors)
    johnny.pencolor(new_color)


screen = Screen()
screen.exitonclick()