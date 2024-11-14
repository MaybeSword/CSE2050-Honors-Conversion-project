from card import Card

class Hand:
    """A Hand of cards in Blackjack.
    """
    def __init__(self):
        """Initialize an empty Hand.
        """
        self.cards = []
        self.value = 0

    def add_card(self, card:Card):
        """Add a Card to this Hand.

        Args:
            card (Card): The card to add.

        Returns:
            Card: The card to add.
        """
        self.cards.append(card)
        self.value += card.card_value()
        if card.rank == 'A' and self.value > 21:
            self.value -= 10
        return card

    def calculate_value(self):
        """Calculate value of this Hand, using standard Blackjack rules.

        Returns:
            int: Value of the Hand.
        """
        return self.value
    
    def __contains__(self, rank):
        """Check if rank is in current Hand.

        Args:
            rank (_type_): Rank of card to check.

        Returns:
            bool: True if rank is in Hand, False otherwise.
        """
        for card in self.cards:
            if card.rank == rank:
                return True
        return False

    def split(self):
        """Splits a Hand with two cards of equal rank into two Hands.

        Returns:
            tuple: Both the current Hand and the new Hand.
        """
        newHand = Hand()
        newHand.add_card(self.cards[1])
        self.cards.pop(1)
        return newHand, self

    def __repr__(self):
        """String representation of Hand.

        Returns:
            str: "hand: (cards in Hand)"
        """
        return f"hand: {self.cards}"

