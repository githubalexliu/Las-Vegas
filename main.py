from Game import Game
from random import randint


def start_game():
    turn_player_num = randint(0, 6)


if __name__ == '__main__':
    game = Game(num_player=5, num_casino=6, num_round=4)
