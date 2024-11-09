class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit.upper()[0]}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    