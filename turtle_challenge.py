#generate a random walk
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")

colors = ["midnight blue","medium sea green","gold","maroon","hot pink","dark slate blue","orange red","dark slate gray"]

direction = [0,90,180,270]
timmy.pensize(5)
timmy.speed("fast")

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))