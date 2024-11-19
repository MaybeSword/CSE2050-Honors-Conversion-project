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
        hand.add_card(deck.deal())
        
        
    
if __name__ == "__main__":
    D1 = Deck()
    Dealer1 = Dealer()
    Dealer1.play_turn(D1)
