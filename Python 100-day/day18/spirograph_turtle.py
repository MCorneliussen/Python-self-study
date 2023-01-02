import turtle as t
from turtle import Screen
from random import choice, randint

t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

johnny = t.Turtle()
johnny.shape("turtle")
johnny.speed("fastest")

current_heading = johnny.heading()

def draw_spiro(gap):
    for _ in range(int(360 / gap)):
        johnny.color(random_color())
        johnny.circle(100)
        johnny.setheading(johnny.heading() + gap)

draw_spiro(2)
screen = Screen()
screen.exitonclick()