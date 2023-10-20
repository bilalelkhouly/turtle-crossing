#Turtle Crossing Game

import time
from turtle import Screen
from obstacle import Obstacles
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
obstacle = Obstacles()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    obstacle.create_obstacle(y=player.ycor())

    # Detect if the player collides with the car
    for car in cars.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    # Detect if the player colliders with an obstacle
    for _ in obstacle.obstacles:
        if _.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    # Detect if the player has reached the top edge of the screen
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        obstacle.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
