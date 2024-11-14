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

    def get_bet(self):
        return self._bet

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
            self._bet = num

    def betCC(self, deck:Deck):
        '''Chris fix this docstring
           Update the bet based on the count rather than player input'''
        if self._bet == 0:
            self._bet = 200
        
        if deck.count> 0:
            if self._bet+50 < self.balance:
                self._bet+=50

        if deck.count<0:
            if self._bet-50 != 0:
                self._bet-=50
        

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

    def playCC(self, deck: Deck, dealer: Dealer):
        # 2 - 6  is plus1, 10 - A, is minus1, 7-9 neutral
        decision = 'stand'
        if self.hand.check_pair():
            if self.hand('A') or self.hand(8):
                decision = 'split'
            if self.hand(2) or self.hand(3) or self.hand(6) or self.hand(7) or self.hand(9):
                if dealer.get_upcard() <7:
                    decision = 'split'
        elif self.hand('A'):
            if self.hand.calculate_value()>12 and self.hand.calculate_value()<16:
                decision = 'hit'
            if self.hand.calculate_value()>15 and self.hand.calculate_value()<19:
                if dealer.get_upcard()<7:
                    decision = 'double'
                else:
                    decision = 'hit'
        else:
            if self.hand.calculate_value()>3 and self.hand.calculate_value()<9:
                decision = 'hit'
            if self.hand.calculate_value() == 9:
                if dealer.get_upcard()<7:
                    decision = 'double'
                else:
                    decision = 'hit'
            if self.hand.calculate_value()>9 and self.hand.calculate_value()<12:
                if dealer.get_upcard()<7:
                    decision = 'double'
                else:
                    if self.hand.calculate_value()>dealer.get_upcard():
                        decision = 'double'
                    else:
                        decision = 'hit'
            if self.hand.calculate_value()>11 and self.hand.calculate_value()<17:
                if dealer.get_upcard()>6:
                    decision = 'hit'

        #add some lines about some advantageous plays using count

        if decision == 'hit': 
            self.hand.add_card()
            self.playCC(deck, dealer)
        if decision == 'split': 
            self.hand.split()
            #call playCC on both hands
        if decision == 'double': 
            self._bet*=2
            self.hand.add_card()