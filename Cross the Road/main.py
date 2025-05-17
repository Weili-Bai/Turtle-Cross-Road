import Other
import time
from Scoreboard import Scoreboard

window = Other.get_window()
player = Other.get_player()
window.onkey(lambda: Other.player_move(player), key="w")
trucks = Other.get_truck_team()
board = Scoreboard(window)
while not Other.is_game_over(player=player, trucks=trucks):
    window.update()
    time.sleep(board.game_speed)
    if not Other.is_paused:
        for truck in trucks:
            Other.truck_move(truck)
    if Other.is_next_level(player):
        Other.is_paused = True
        Other.initial_position(player)
        board.level += 1
        Other.MOVE_STEP += 1
        board.write_board()
        board.game_speed *= 0.95
over = Other.game_over()
window.exitonclick()
