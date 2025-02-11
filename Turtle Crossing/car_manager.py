from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCRIEMENT = 10
N_CARS = 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.n_cars = N_CARS
        self.cars_ls = []

    def create_init_cars(self):
        self.clear_screen()
        for i in range(self.n_cars):
            new_car = self.create_car()
            self.cars_ls.append(new_car)

    def random_coords(self, y_range, x_range):
        y_position = random.randint(y_range[0], y_range[1])
        x_position = random.randint(x_range[0], x_range[1])
        return x_position, y_position

    def create_car(self):
        colour = random.choice(COLOURS)
        x, y = self.random_coords(y_range=(-250, 250), x_range=(-250, 250))
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(colour)
        new_car.penup()
        new_car.goto(x, y)
        return new_car

    def move_cars(self):
        for car in self.cars_ls:
            car.backward(self.car_speed)

    def reset_car(self):
        for car in self.cars_ls:
            if car.xcor() < -300:
                x, y = self.random_coords(y_range=(-250, 250), x_range=(300, 400))
                car.goto(x, y)

    def clear_screen(self):
        for car in self.cars_ls:
            car.hideturtle()
            del car
        self.cars_ls = []
