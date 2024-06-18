#challange to draw dashed line square using turtle 
from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("green")

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

timmy.right(90)

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

timmy.right(90)

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

timmy.right(90)

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()
