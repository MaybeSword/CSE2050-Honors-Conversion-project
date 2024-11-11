class Card:
    def __init__(self, rank, suit, faceup = True):
        '''Initializes a card object'''
        self.rank = rank
        self.suit = suit
        self.faceup = faceup

    def card_value(self):
        val = 0
        L_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        face_cards = ['J', 'Q', 'K']
        if self.rank in L_nums:
            val = self.rank
        elif self.rank in face_cards:
            val = 10
        else: 
            val += 11
        return val

    def __repr__(self):
        if self.faceup: return f"{self.rank}{self.suit.upper()[0]}"
        else: return "???"

    def __str__(self):
        if self.faceup: return f"{self.rank} of {self.suit}"
        else: return "??? of ???"
    