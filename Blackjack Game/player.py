from hand import Hand
from deck import Deck
from dealer import Dealer

class Player:
    """Player to play the game of Blackjack.
    """ 
    def __init__(self, balance=2500):
        """Initialize a Player.

        Args:
            balance (int, optional): Player's Money. Defaults to 2500.
        """
        self.hand = Hand()
        self.balance = balance
        self._bet = 0
        self.busted = False
        self.blackjack = False

    def get_bet(self):
        """Returns the player's bet.

        Returns:
            int: Player's bet
        """
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
        """Updates bet based on count.

        Args:
            deck (Deck): The Deck we are counting.
        """
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

    def play_action(self, hand:Hand, deck:Deck, action):
        """Play the hand manually.

        Args:
            hand (Hand): Hand to play with/alter.
            deck (Deck): Deck to play from.
        """
        #actions stand, hit, double, split if ranks equal
        if action == "hit":
            hand.add_card(deck.deal())
        if action == "double":
            self.bet(self._bet * 2)
            hand.add_card(deck.deal())
        if action == "split":
            newHands = hand.split()
            return newHands
        if len(hand.cards) == 2 and hand.calculate_value() == 21: # Player has gotten a blackjack
            self.blackjack = True
        if hand.calculate_value() > 21: # Player has busted
            self.busted = True
        return None

    def basic_strategy_play(self):
        pass

    def playCC(self, deck: Deck, dealer: Dealer):
        """Plays Blackjack using an optimal counting cards strategy.

        Args:
            deck (Deck): Deck we are counting.
            dealer (Dealer): Dealer we are playing against.
        """
        # 2 - 6  is plus1, 10 - A, is minus1, 7-9 neutral
        decision = 'stand'
        if self.hand.check_pair():
            if 'A' in self.hand or 8 in self.hand:
                decision = 'split'
            if 2 in self.hand or 3 in self.hand or 6 in self.hand or 7 in self.hand or 9 in self.hand:
                if dealer.get_upcard() <7:
                    decision = 'split'
        elif 'A' in self.hand:
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
        if 'A' in self.hand and 5 in self.hand and len(self.hand.cards) ==2:
            if dealer.get_upcard()==4:
                if deck.count>=3:
                    decision = 'double'
                else:
                    decision = 'hit'

        if self.hand.calculate_value() == 10:
            if dealer.hand.get_upcard() == 10:
                decision = 'double' if deck.count>=4 else decision='hit'

        if self.hand.calculate_value() == 16:
            if dealer.hand.get_upcard() == 10:
                if deck.count >= 0:
                    decision = 'stand'
                else:
                    decision = 'hit'
        
        if self.hand.calculate_value() == 15:
            if dealer.hand.get_upcard() == 10:
                if deck.count >= 4:
                    decision = 'stand'
                else:
                    decision = 'hit'
        
        if self.hand.check_pair():
            if len(self.hand.cards) == 2:
                if 10 in self.hand:
                    if dealer.hand.get_upcard() == 5 or dealer.hand.get_upcard() == 6:
                        if deck.count>=5:
                            decision = 'split'

        if self.hand.check_pair():
            if len(self.hand.cards) == 2:
                if 4 in self.hand:
                    if dealer.hand.get_upcard() == 5 or dealer.hand.get_upcard() == 6:
                        if deck.count>=4:
                            decision = 'split'

        if decision == 'hit': 
            self.hand.add_card()
            self.playCC(deck, dealer)
        if decision == 'split': 
            self.hand.split()
            #call playCC on both hands
        if decision == 'double': 
            self._bet*=2
            self.hand.add_card()