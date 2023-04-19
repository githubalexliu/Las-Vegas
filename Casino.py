class Casino:
    def __init__(self, name):
        self.bill = []
        self.bet = {}
        self.name = name

    def set_bill(self, bill):
        self.bill = bill

    def print_bill(self):
        print(f'Casino {self.name} has bills ${", $".join(map(str, self.bill))}')

    def clear_bet(self):
        self.bet = {}

    def update_bet(self, name, dice):
        self.bet[name] = dice
        # print('Casino ' + self.name + )
