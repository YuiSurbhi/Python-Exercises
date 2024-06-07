#challange to draw different shapes 
from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")

#drawing square
timmy.color("red")

timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

#drawing pentagon
timmy.color("green")

for _ in range (5):
    timmy.right(72)
    timmy.forward(100)

#drawing triangle 
timmy.color("dark blue")

for _ in range (3):
    timmy.right(120)
    timmy.forward(100)

#drawing hexagon 
timmy.color("blue")

for _ in range(6):
    timmy.right(60)
    timmy.forward(100)

#drawing heptagon
timmy.color("orange")

for _ in range (7):
    timmy.right(51.4)
    timmy.forward(100)

#drawing octagon 
timmy.color("purple")

for _ in range(8):
    timmy.right(45)
    timmy.forward(100)

#drawing nonagon
timmy.color("pink")

for _ in range(9):
    timmy.right(40)
    timmy.forward(100)

#drawing decagon
timmy.color("dark green")

for _ in range(10):   
    timmy.right(36)
    timmy.forward(100)
screen.exitonclick()