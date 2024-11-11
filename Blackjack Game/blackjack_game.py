from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand

class BlackjackGame:
    """A Blackjack Game.
    """
    def __init__(self):
        """Initialize a BlackjackGame.
        """
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.dealer_hand = Hand()
        self.player_hand = Hand()
    
    def before_game(self):
        """Betting phase of BlackjackGame.
        """
        #prompt player for bet
        self.player.bet(500) #arbitrary value

    def start_game(self):
        """Initial 4 cards dealt in BlackjackGame.
        """
        self.dealer_hand.add_card(self.deck.deal(faceup=False))
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

    def player_turn(self):
        """Player's turn in BlackjackGame.
        """
        self.player.play()

    def dealer_turn(self):
        """Dealer's turn in BlackjackGame.
        """
        self.dealer_hand.cards[0].faceup = True
        if not self.player.busted:
            self.dealer.play_turn()
        

    def check_winner(self):
        """Checks the winner of the BlackjackGame, between Dealer and Player.
        """
        if self.player.blackjack:
            if self.dealer.blackjack:
                #push
                pass
            else:
                self.player.update_balance(loss=True, blackjack=True)
        elif self.dealer.blackjack and self.player_hand.calculate_value() == 21:
            #dealer wins
            self.player.update_balance(loss=True)
        elif self.player.is_busted():
            #dealer wins
            self.player.update_balance(loss=True)
        elif self.dealer.is_busted():
            #player wins
            self.player.update_balance(loss=False)
        elif self.dealer_hand.calculate_value() > self.player_hand.calculate_value():
            #dealer wins
            self.player.update_balance(loss=True)
        elif self.dealer_hand.calculate_value() < self.player_hand.calculate_value():
            #player wins
            self.player.update_balance(loss=False)
        else:
            #push
            pass

class BlackjackGameCC:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        self.dealt_cards = []
    
    def before_game(self):
        #prompt player for bet
        self.player.bet(500) #arbitrary value

    def start_game(self):
        self.dealer_hand.add_card(self.deck.deal(faceup=False))
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

    def player_turn(self):
            self.player.playCC()

    def dealer_turn(self):
        self.dealer_hand.cards[0].faceup = True
        if not self.player.busted:
            self.dealer.play_turn()
        

    def check_winner(self):
        if self.player.blackjack:
            if self.dealer.blackjack:
                #push
                pass
            else:
                self.player.update_balance(loss=True, blackjack=True)
        elif self.dealer.blackjack and self.player_hand.calculate_value() == 21:
            #dealer wins
            self.player.update_balance(loss=True)
        elif self.dealer_hand.calculate_value() > self.player_hand.calculate_value():
            if not self.dealer.is_busted():
                #dealer wins
                self.player.update_balance(loss=True)
                pass
            else:
                #player wins
                self.player.update_balance(loss=False)
                pass
        elif self.dealer_hand.calculate_value() < self.player_hand.calculate_value():
            if not self.player.is_busted():
                #player wins
                self.player.update_balance(loss=False)
                pass
            else: 
                # dealer wins
                self.player.update_balance(loss=True)
                pass
        else:
            #push
            pass