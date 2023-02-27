class Casino:
    def __init__(self, name):
        self.bill = []
        self.bet = {}
        self.name = name

    def set_bill(self, bill):
        self.bill = bill

    def print_bill(self):
        print('Casino ' + self.name + ' has bills $' + ', $'.join(map(str, self.bill)))
