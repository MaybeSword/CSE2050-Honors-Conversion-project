from hand import Hand
from deck import Deck

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def play_turn(self, deck):
        while self.hand.calculate_value() <= 16:
            # dealer hit in some way implemented
            pass
