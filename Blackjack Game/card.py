class Card:
    def __init__(self, rank, suit, faceup = True):
        '''Initializes a card object'''
        self.rank = rank
        self.suit = suit
        self.faceup = faceup

    def __repr__(self):
        if self.faceup: return f"{self.rank}{self.suit.upper()[0]}"
        else: return "???"

    def __str__(self):
        if self.faceup: return f"{self.rank} of {self.suit}"
        else: return "??? of ???"
    