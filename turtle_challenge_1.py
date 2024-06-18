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

#another way to draw different shapes using turtle 
import turtle as t
import random 

timmy = t.Turtle()
timmy.shape("turtle")

colors = ["midnight blue","medium sea green","gold","maroon","hot pink","dark slate blue","orange red","dark slate gray"]

def draw_shapes(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_side_n)
