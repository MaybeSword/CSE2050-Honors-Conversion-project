from hand import Hand
from deck import Deck
from time import sleep

class Dealer:
    """A Dealer to deal in Blackjack.
    """
    def __init__(self):
        """Initialize a Dealer.
        """
        self.hand = Hand()
        self.busted = False
        self.blackjack = False

    def get_upcard(self):
        return self.hand.cards[1].card_value()

    def is_busted(self):
        """Check if dealer has busted.

        Returns:
            bool: True if dealer has busted, False otherwise.
        """
        return self.busted   

    def play_turn(self, hand:Hand, deck:Deck):
        """Plays the dealer's turn.

        Args:
            hand (Hand): Dealer's hand.
            deck (Deck): Deck to pull from.
        """
        while hand.calculate_value() <= 16:
            hand.add_card(deck.deal())
        if hand.calculate_value() > 21:
            self.busted = True
        if len(hand.cards) == 2 and hand.calculate_value() == 21:
            self.blackjack = True
        return hand
        
        
    
if __name__ == "__main__":
    D1 = Deck()
    Dealer1 = Dealer()
    Dealer1.play_turn(D1)
