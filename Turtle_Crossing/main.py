import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

cars.create_init_cars()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # 0.1 seconds delay
    screen.update()

    cars.move_cars()
    cars.reset_car()
    for car in cars.cars_ls:
        if player.distance(car) < 20:
            player.reset_player()
            cars.clear_screen()
            scoreboard.game_over()
            time.sleep(3)
            game_is_on = False  # End the game

        if player.is_at_finish_line():
            scoreboard.level_up()
            cars.level_up()  # Increase the number of cars and speed

screen.exitonclick()
