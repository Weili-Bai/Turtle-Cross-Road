import random
import turtle
from turtle import Screen, Turtle

import Other
import Scoreboard

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
TRUCK_QUANTITY = 20
MOVE_STEP = 5
turtle.colormode(255)
is_paused = True


def get_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def get_player():
    result = Turtle()
    result.shape("turtle")
    result.setheading(90)
    result.penup()
    initial_position(result)
    return result


def get_window():
    result = Screen()
    result.title("Turtle Cross Road")
    result.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
    result.tracer(0)
    result.listen()
    return result


def player_move(player):
    player.forward(20)
    Other.is_paused = False


def is_next_level(player):
    y = player.ycor()
    return y >= WINDOW_WIDTH / 2 - 10


def initial_position(player):
    y = WINDOW_WIDTH / -2 + 20
    player.goto(0, y)


def get_square(part):
    part.shape("square")
    part.penup()
    part.setheading(180)


def get_truck():
    result = []
    front = Turtle()
    back = Turtle()
    get_square(front)
    get_square(back)
    colour = get_colour()
    front.color(colour, colour)
    back.color(colour, colour)
    result.append(front)
    result.append(back)
    initial_truck_position(result)
    return result


def initial_truck_position(truck):
    y = random.randint(20 - int(WINDOW_HEIGHT / 2), int(WINDOW_HEIGHT / 2) - 20)
    truck[0].goto(WINDOW_WIDTH / 2, y)
    truck[1].goto(WINDOW_WIDTH / 2 + 20, y)


def truck_move(truck):
    truck[0].forward(MOVE_STEP)
    truck[1].forward(MOVE_STEP)
    if truck[1].xcor() < WINDOW_WIDTH / -2 - 10:
        initial_truck_position(truck)


def get_truck_team():
    result = []
    for _ in range(0, TRUCK_QUANTITY):
        curr = get_truck()
        x = random.randint(60 - int(WINDOW_WIDTH / 2), 10 + int(WINDOW_WIDTH / 2))
        y = random.randint(40 - int(WINDOW_HEIGHT / 2), int(WINDOW_HEIGHT / 2) - 40)
        curr[0].goto(x, y)
        curr[1].goto(x + 20, y)
        result.append(curr)
    return result


def is_game_over(player, trucks):
    for truck in trucks:
        if truck[0].distance(player) < 20 or truck[1].distance(player) < 20:
            return True
    return False


def game_over():
    result = Turtle()
    result.penup()
    result.goto(0, 0)
    result.hideturtle()
    result.write("GAME OVER!", align="center", font=Scoreboard.FONT)
    return result
