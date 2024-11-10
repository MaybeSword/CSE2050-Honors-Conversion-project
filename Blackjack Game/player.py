from hand import Hand
from deck import Deck

class Player:
    def __init__(self, balance=0):
        self.hand = Hand()
        self.balance = balance

    def play(self, deck=Deck):
        """playing manually"""
        #actions stand, hit, double, split if ranks equal
        pass

    def count_cards_play(self):
        # 2 - 6  is plus1, 10 - A, is minus1, 7-9 neutral
        pass
