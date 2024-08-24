from turtle import Turtle
import random
from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [(-310, 0), (-330, 0)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT






