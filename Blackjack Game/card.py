class Card:
    """A playing card.
    """
    def __init__(self, rank, suit:str, faceup = True):
        """Initialize a Card.

        Args:
            rank (_type_): Rank of the card, 2 - A.
            suit (str): Suit of the card, Hearts, Spades, Clubs, or Diamonds.
            faceup (bool, optional): True if the card is face up, False otherwise. Defaults to True.
        """
        card_dict = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A': 11}
        self.val = card_dict[rank]
        self.rank = rank
        self.suit = suit
        self.faceup = faceup

    def card_value(self):
        """Returns the card value

        Returns:
            int: value of the Card
        """
        return self.val

    def __repr__(self):
        """Minimal string representation of Card. 

        Returns:
            str: Rank and Suit back to back, Ace of hearts would be 'AH'
        """
        if self.faceup: return f"{self.rank}{self.suit.upper()[0]}"
        else: return "???"

    def __str__(self):
        """String representation of Card

        Returns:
            str: Rank of Suit, Ace of hearts would be "A of hearts"
        """
        if self.faceup: return f"{self.rank} of {self.suit}"
        else: return "??? of ???"
    