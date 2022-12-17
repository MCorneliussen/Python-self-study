from turtle import Turtle, Screen

johnny = Turtle()
johnny.shape("turtle")
johnny.color("black", "darkgreen")

for _ in range(4):
    johnny.right(90)
    johnny.forward(100)

screen = Screen()
screen.exitonclick()