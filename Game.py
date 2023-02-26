from Casino import Casino
from Player import Player
from random import shuffle, randint


class Game:
    def __init__(self, num_player, num_casino, num_round):
        self.players = [Player(human=True)] + [Player() for i in range(num_player - 1)]
        self.casinos = [Casino() for i in range(num_casino)]
        self.casino_bill = []
        self.num_casino = num_casino
        self.num_player = num_player

    def generate_casino_bill(self, num_casino, min_bill_per_casino, min_amount):
        bills = list(range(10000, 100000, 10000)) * 6
        shuffle(bills)
        list_bills = []
        for i in range(num_casino):
            casino_bill = []
            while sum(casino_bill) < min_amount or len(casino_bill) < min_bill_per_casino:
                casino_bill.append(bills.pop())
            list_bills.append(sorted(casino_bill, reverse=True))
        self.casino_bill = sorted(list_bills, reverse=True, key=lambda x: (sum(x), max(x)))

    def set_casino_bill(self):
        [self.casinos[i].set_bill(self.casino_bill[i]) for i in range(self.num_casino)]