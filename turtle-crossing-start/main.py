import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car = CarManager()
board= Scoreboard()
screen.onkey(player.go_up,"Up")
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    #Detect collision with cars
    for cars in car.all_cars:
        if cars.distance(player) <20:
            game_is_on =False
            board.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        car.increase_speed()
        board.increment()


screen.exitonclick()
