class Player:
    def __init__(self, name='', human=False):
        self.score = 0
        self.token = 0
        self.dice = 0
        # name = input('What is your name?') if human else name
        self.name = 'Z' if not name else name
        self.human = human

    def init_round(self, token, dice):
        self.token, self.dice = token, dice
