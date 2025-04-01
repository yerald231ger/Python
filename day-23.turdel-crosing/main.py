import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

target_fps = 120
frame_time = 1 / target_fps

game_is_on = True
last_time = time.time()
while game_is_on:
    current_time = time.time()
    delta = current_time - last_time
    if delta >= frame_time:
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        #Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        #Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

        last_time = current_time

screen.exitonclick()
