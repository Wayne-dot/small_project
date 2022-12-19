from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.move_distance = 0
        self.move_distance += STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            n_car = Turtle()
            n_car.penup()
            n_car.shape("square")
            n_car.shapesize(stretch_len=2)
            n_car.color(random.choice(COLORS))
            new_y = random.randint(-240, 240)
            n_car.goto(300, new_y)
            self.all_car.append(n_car)

    def car_move(self):
        for car in self.all_car:
            car.backward(self.move_distance)

    def car_speed_increase(self):
        self.move_distance += MOVE_INCREMENT
