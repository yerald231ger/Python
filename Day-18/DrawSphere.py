# Write spirograph patterns to a turtle graphics window

import turtle
import math
import random

# Set up the screen
turtle.setup(800, 600)
turtle.title("Spirographs!")

window = turtle.Screen()

# Set up the turtle
spiro = turtle.Turtle()
spiro.speed("fastest")
spiro.width(2)

# Set up the parameters for the spirograph
R = 125
r = 75
d = 125

# Set up the color palette
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
def random_color():
    return random.choice(colors)

for _ in range(0, 36):
    spiro.color(random_color())
    spiro.circle(100)
    spiro.setheading(spiro.heading() + 10)


window.exitonclick()




