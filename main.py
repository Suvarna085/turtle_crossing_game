import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish():
        print("Player reached the finish line!")
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()
        print(f"Level: {scoreboard.level}")

screen.exitonclick()