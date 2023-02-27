from Casino import Casino
from Player import Player
from random import shuffle, randint


class Game:
    def __init__(self, num_player, num_casino, num_round):
        self.players = [Player(human=True)] + [Player() for i in range(num_player - 1)]
        self.casinos = [Casino(str(i + 1)) for i in range(num_casino)]
        self.num_casino = num_casino
        self.num_player = num_player

    def generate_casino_bill(self, min_bill_per_casino=2, min_amount=50000, min_bill_value=10000,
                             max_bill_value=100000, increment_bill=10000):
        bills = list(range(min_bill_value, max_bill_value, increment_bill)) * self.num_casino
        shuffle(bills)
        list_bills = []
        for i in range(self.num_casino):
            casino_bill = []
            while sum(casino_bill) < min_amount or len(casino_bill) < min_bill_per_casino:
                casino_bill.append(bills.pop())
            list_bills.append(sorted(casino_bill, reverse=True))
        return sorted(list_bills, reverse=True, key=lambda x: (sum(x), max(x)))

    def set_casino_bill(self):
        casino_bill = self.generate_casino_bill()
        [self.casinos[i].set_bill(casino_bill[i]) for i in range(self.num_casino)]

    def print_casino_bill(self):
        [casino.print_bill() for casino in self.casinos]

    def init_round(self):
        self.set_casino_bill()
        self.print_casino_bill()
