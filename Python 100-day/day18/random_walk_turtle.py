import turtle as t
from turtle import Screen
from random import choice, randint

t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


johnny = t.Turtle()
johnny.shape("turtle")
johnny.pensize(10)
johnny.speed(0)


direction = [0, 90, 180, 270]

for _ in range(500):
    johnny.pencolor(random_color())
    johnny.setheading(choice(direction))
    johnny.forward(25)



screen = Screen()
screen.exitonclick()