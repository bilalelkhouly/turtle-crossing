import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_PROBABILITY = 12


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.probability = STARTING_PROBABILITY

    def create_car(self):
        if random.randint(1,self.probability) == self.probability:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        self.probability -= 2
