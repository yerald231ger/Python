from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game settings
target_fps = 60
frame_time = 1 / target_fps
move_delay = 0.05  # Faster movement update for smoothness

game_is_on = True
last_time = time.time()
last_move_time = time.time()

while game_is_on:
    current_time = time.time()
    delta = current_time - last_time
    
    if delta >= frame_time:
        screen.update()
        last_time = current_time
        
        # Move snake more frequently for smoother motion
        if current_time - last_move_time >= move_delay:
            snake.move()
            last_move_time = current_time

            #Detect collision with food.
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()

            #Detect collision with wall.
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                scoreboard.reset()
                snake.reset()
            #Detect collision with tail.
            for segment in snake.segments[1:]:
                if segment == snake.head:
                    pass
                elif snake.head.distance(segment) < 10:
                    scoreboard.reset()
                    snake.reset()
screen.exitonclick()
