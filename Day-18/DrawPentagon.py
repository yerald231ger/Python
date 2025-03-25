import turtle


def define_turtle() -> turtle.Turtle:
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.speed(10)
    return brad


def define_window():
    window = turtle.Screen()
    window.bgcolor("red")
    return window

def draw_a_pentagon(size: int, brad: turtle.Turtle):
    for i in range(1, 6):
        brad.forward(size)
        brad.right(72)

def center_turtle(brad, size):
    brad.penup()
    brad.goto(-(size / 2), +(size / 2))
    brad.pendown()


SIZE = int(input("Enter the size of the square: "))
BRAD = define_turtle()
WINDOW = define_window()

center_turtle(BRAD, SIZE)
draw_a_pentagon(SIZE, BRAD)

WINDOW.exitonclick()