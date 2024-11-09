from hand import Hand

class Player:
    def __init__(self, balance):
        self.hand = Hand()
        self.balance = balance

    def count_cards_play(self):
        # 2 - 6  is plus1, 10 - A, is minus1, 7-9 neutral
        pass
