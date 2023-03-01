import collections
from random import randint


class Player:
    def __init__(self, name='', human=False):
        self.score = 0
        self.token = 0
        self.dice = 0
        # name = input('What is your name?') if human else name
        self.name = 'Player' if not name else name
        self.human = human
        self.dice_result = {}

    def init_round(self, token, dice):
        self.token += token
        self.dice += dice

    def roll_dice(self):
        self.dice_result = collections.Counter([randint(1, 6) for _ in range(self.dice)])
        for i in range(1, 7):
            if i not in self.dice_result:
                self.dice_result[i] = 0
        self.dice_result = dict(sorted(self.dice_result.items()))
