from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand

class BlackjackGame:
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
            self.player.play()

    def dealer_turn(self):
        self.dealer_hand.cards[0].faceup = True
        if not self.player.busted:
            self.dealer.play_turn()
        

    def check_winner(self):
        if self.dealer_hand.calculate_value() > self.player_hand.calculate_value():
            if not self.dealer_hand.is_busted():
                #dealer wins
                pass
            else:
                #player wins
                pass
        elif self.dealer_hand.calculate_value() < self.player_hand.calculate_value():
            if not self.player_hand.isbusted():
                #player wins
                pass
            else: 
                # dealer wins
                pass
        else:
            #push
            pass
