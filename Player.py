from collections import Counter
from random import randint, choice


class Player:
    def __init__(self, name='', is_human=False):
        self.score = 0
        self.token = 0
        self.dice = 0
        # name = input('What is your name?') if human else name
        self.name = 'Player 1' if not name else name
        self.is_human = is_human
        self.dice_result = {}

    def init_round(self, token, dice):
        self.token += token
        self.dice += dice

    def roll_dice(self):
        assert self.dice > 0
        self.dice_result = Counter([str(randint(1, 6)) for _ in range(self.dice)])
        print('Dice result: ' + ''.join([key * value for key, value in sorted(self.dice_result.items())]))
        return sorted(self.dice_result.keys())

    def choose_casino(self):
        casino_options = self.roll_dice()
        casino_choice = ''
        if self.is_human:
            while casino_choice not in casino_options:
                token_message = f"You may also choose 't' to use a token (Token: {str(self.token)})" \
                    if self.token > 0 else ''
                casino_choice = input('Please choose a casino in ' + ','.join(casino_options) +
                                      ". " + token_message)
                if self.token > 0 and casino_choice == 't':
                    casino_options = self.roll_dice()
                    self.token -= 1
        else:
            casino_choice = choice(casino_options)
        print(f'{self.name} places {str(self.dice_result[casino_choice])} dice on Casino {casino_choice}')
        self.dice -= self.dice_result[casino_choice]
        return {'casino': casino_choice, 'dice': self.dice_result[casino_choice]}
