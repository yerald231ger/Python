import turtle


def define_turtle() -> turtle.Turtle:
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)
    return brad


def define_window():
    window = turtle.Screen()
    window.bgcolor("red")
    return window


def draw_square(size: int, brad: turtle.Turtle):
    for i in range(1, 5):
        draw_dashed_line(brad, size)
        brad.right(90)


def draw_dashed_line(brad, size):
    steps: int = 3
    counter: int = 0
    remaining: int = size
    draw = True
    while remaining > 0:
        if draw:
            brad.pendown()
        else:
            brad.penup()

        brad.forward(1)
        counter += 1
        remaining -= 1
        if counter == steps:
            draw = not draw
            counter = 0


def center_turtle(brad, size):
    brad.penup()
    brad.goto(-(size / 2), +(size / 2))
    brad.pendown()


square_size = int(input("Enter the size of the square: "))
BRAD = define_turtle()
WINDOW = define_window()

center_turtle(BRAD, square_size)
draw_square(square_size, BRAD)

WINDOW.exitonclick()
