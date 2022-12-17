from turtle import Turtle, Screen

johnny = Turtle()
johnny.shape("turtle")
johnny.color("black", "darkgreen")

for _ in range(15):
    johnny.pendown()
    johnny.forward(10)
    johnny.penup()
    johnny.forward(10)

screen = Screen()
screen.exitonclick()