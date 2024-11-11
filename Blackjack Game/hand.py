from card import Card

class Hand:
    """A Hand of cards in Blackjack.
    """
    def __init__(self):
        """Initialize an empty Hand.
        """
        self.cards = []

    def add_card(self, card:Card):
        """Add a Card to this Hand.

        Args:
            card (Card): The card to add.

        Returns:
            Card: The card to add.
        """
        self.cards.append(card)
        return card

    def calculate_value(self):
        """Calculate value of this Hand, using standard Blackjack rules.

        Returns:
            int: Value of the Hand.
        """
        val = 0
        L_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        face_cards = ['J', 'Q', 'K']
        for card in self.cards:
            if card.rank in L_nums:
                val += card.rank
            elif card.rank in face_cards:
                val += 10
            else: 
                val += 11
                if val > 21:
                    val -= 10
        return val

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

