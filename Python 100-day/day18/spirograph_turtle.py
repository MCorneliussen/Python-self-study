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
johnny.speed(100)

current_heading = johnny.heading()

def draw_spiro(gap):
    for _ in range(500 / gap):
        johnny.color(random_color())
        johnny.circle(100)
        johnny.setheading(johnny.heading() + gap)

draw_spiro(5)
screen = Screen()
screen.exitonclick()