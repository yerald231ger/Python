def turn_left():
    print("")


def right_is_clear():
    return True


def move():
    print("")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while right_is_clear():
        move()
    turn_right()
