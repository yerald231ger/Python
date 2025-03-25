# Random walk with turtle graphics
import random
import turtle

def define_turtle() -> turtle.Turtle:
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.speed(1)
    brad.pensize(10)
    return brad


def define_window():
    window = turtle.Screen()
    return window


def random_walk(brad: turtle.Turtle, steps: int):
    for i in range(1, steps):
        # Change the color of the turtle
        brad.color(random.choice(["#8ED081", "#3D5A80", "#98C1D9", "#EE6C4D", "#293241"]))
        # Change the direction of the turtle
        direction = random.choice(["left", "right"])
        if direction == "left":
            brad.left(90)
        elif direction == "right":
            brad.right(90)
        brad.forward(random.choice([30, 50, 70]))

BRAD = define_turtle()
WINDOW = define_window()

random_walk(BRAD, 100)

WINDOW.exitonclick()