from turtle import Turtle, Screen
import threading

tim = Turtle()
screen = Screen()


def key_up():
    tim.forward(10)


def key_down():
    tim.backward(10)


def key_left():
    tim.left(10)


def key_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key_down, "Down")
screen.onkey(key_up, "Up")
screen.onkey(key_left, "Left")
screen.onkey(key_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
