from hand import Hand
from deck import Deck
from dealer import Dealer

class Player:
    """Player to play the game of Blackjack.
    """ 
    def __init__(self, balance=1000):
        """Initialize a Player.

        Args:
            balance (int, optional): Player's Money. Defaults to 1000.
        """
        self.hand = Hand()
        self.balance = balance
        self._bet = 0
        self.busted = False
        self.blackjack = False

    def bet(self, num):
        """Bet an amount of money equal to num.

        Args:
            num (int): Amount of bet.

        Raises:
            RuntimeError: If the bet exceeds player's balance.
        """
        if self._bet > self.balance:
            raise RuntimeError("Not enough money!")
        else:
            self.bet == num

    def update_balance(self, loss: bool, blackjack=False):
        """Update player's balance after a hand.

        Args:
            loss (bool): True if player lost hand, False if player won hand.
            blackjack (bool, optional): True if player got a Blackjack. Defaults to False.
        """
        if blackjack:
            self.balance += int(1.5*self._bet)
        elif loss:
            self.balance -= self._bet
        else:
            self.balance += self._bet

    def is_busted(self):
        """Check if player has busted.

        Returns:
            bool: True if player busted, False if player didn't bust.
        """
        return self.busted

    def play(self, hand:Hand, deck:Deck):
        """Play the hand manually.

        Args:
            hand (Hand): Hand to play with/alter.
            deck (Deck): Deck to play from.
        """
        #actions stand, hit, double, split if ranks equal
        if len(hand.cards) == 2 and hand.calculate_value() == 21: # Player has gotten a blackjack
            self.blackjack = True
        if hand.calculate_value() > 21: # Player has busted
            self.busted = True

    def basic_strategy_play(self):
        pass

    def playCC(self, count, dealer: Dealer):
        # 2 - 6  is plus1, 10 - A, is minus1, 7-9 neutral
        if self.hand.check_pair() == True:
            if self.hand('A') or self.hand(8):
                self.hand.split()
            if self.hand(2) or self.hand(3) or self.hand(6) or self.hand(7) or self.hand(9):
                if dealer.get_upcard() <7:
                    self.hand.split()
