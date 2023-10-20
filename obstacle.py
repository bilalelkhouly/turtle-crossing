import random
from turtle import Turtle

STARTING_PROBABILITY = 25


class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.obstacles = []
        self.hideturtle()
        self.probability = STARTING_PROBABILITY

    def create_obstacle(self, y):
        if random.randint(1, self.probability) == self.probability:
            new_obstacle = Turtle("square")
            new_obstacle.shapesize(stretch_wid=0.25, stretch_len=1)
            new_obstacle.penup()
            new_obstacle.color("red")
            new_obstacle.right(90)
            random_y = random.randint(int(y) + 10, 300)
            random_x = random.randint(-250, 250)
            new_obstacle.goto(random_x, random_y)
            self.obstacles.append(new_obstacle)

    def level_up(self):
        self.probability -= 5
