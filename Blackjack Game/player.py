from hand import Hand
from deck import Deck

class Player:
    def __init__(self, balance=0):
        self.hand = Hand()
        self.balance = balance
        self._bet = 0
        self.busted = False

    def bet(self, numm):
        if self._bet > self.balance:
            raise RuntimeError("Not enough money!")

    def os_busted(self):
        return self.busted

    def play(self, hand, deck=Deck):
        """playing manually"""
        #actions stand, hit, double, split if ranks equal
        if hand.calculate_value() > 21:
            self.busted = True

    def basic_strategy_play(self):
        pass

    def count_cards_play(self, past_cards=[]):
        # 2 - 6  is plus1, 10 - A, is minus1, 7-9 neutral
        pass
