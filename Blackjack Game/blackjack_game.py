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
    
    def reset(self):
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
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        self.player.busted, self.dealer.busted, self.player.blackjack, self.dealer.blackjack = False, False, False, False
        self.dealer_hand.add_card(self.deck.deal(faceup=False))
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

    def player_turn(self, action):
        """Player's turn in BlackjackGame.
        """
        if self.player.play_action(self.player_hand, self.deck, action) != None:
            #talk to parent controller class somehow
            pass

    def dealer_turn(self):
        """Dealer's turn in BlackjackGame.
        """
        self.dealer_hand.cards[0].faceup = True
        if not self.player.busted:
            self.dealer.play_turn(self.dealer_hand, self.deck)
        

    def check_winner(self):
        """Checks the winner of the BlackjackGame, between Dealer and Player.
        """
        if self.player.blackjack:
            if self.dealer.blackjack:
                return "It's a tie!"
            else:
                self.player.update_balance(loss=False, blackjack=True)
                return "Player wins + blackjack!"
        elif self.dealer.blackjack and self.player_hand.calculate_value() == 21:
            self.player.update_balance(loss=True)
            return "Dealer wins!"
        elif self.player.is_busted():
            self.player.update_balance(loss=True)
            return "Player busts! Dealer wins."
        elif self.dealer.is_busted():
            self.player.update_balance(loss=False)
            return "Dealer busts! Player wins."
        elif self.dealer_hand.calculate_value() > self.player_hand.calculate_value():
            self.player.update_balance(loss=True)
            return "Dealer wins!"
        elif self.dealer_hand.calculate_value() < self.player_hand.calculate_value():
            self.player.update_balance(loss=False)
            return "Player wins!"
        else:
            return "It's a tie!"

class BlackjackGameCC:
    """A Blackjack game, implementing counting cards.
    """
    def __init__(self):
        """Initialize a BlackjackGameCC.
        """
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        self.dealt_cards = []
    
    def before_game(self):
        """Betting phase. Use optimal betting techniques."
        """
        self.player.betCC(self.deck)

    def start_game(self):
        """Initial phase of game. First four cards dealt.
        """
        self.dealer_hand.add_card(self.deck.deal(faceup=False))
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

    def player_turn(self):
        """Optimal counting cards algorithm's turn to play.
        """
        self.player.playCC()

    def dealer_turn(self):
        """Dealer's turn in Blackjack.
        """
        self.dealer_hand.cards[0].faceup = True
        if not self.player.busted:
            self.dealer.play_turn(self.dealer_hand, self.deck)
        

    def check_winner(self):
        """Checks the winner of the hand. 
        """
        if self.player.blackjack:
            if self.dealer.blackjack:
                #push
                pass
            else:
                self.player.update_balance(loss=False, blackjack=True)
        elif self.dealer.blackjack and self.player_hand.calculate_value() == 21:
            print("dealer wins")
            self.player.update_balance(loss=True)
        elif self.dealer_hand.calculate_value() > self.player_hand.calculate_value():
            if not self.dealer.is_busted():
                print("dealer wins")
                self.player.update_balance(loss=True)
                pass
            else:
                print("player wins")
                self.player.update_balance(loss=False)
                pass
        elif self.dealer_hand.calculate_value() < self.player_hand.calculate_value():
            if not self.player.is_busted():
                print("player wins")
                self.player.update_balance(loss=False)
                pass
            else: 
                print("dealer wins")
                self.player.update_balance(loss=True)
                pass
        else:
            #push
            pass



if __name__ == "__main__":
    BG = BlackjackGame()
    BG.before_game()
    BG.start_game()
    print(f"dealer hand: {BG.dealer_hand}, player hand: {BG.player_hand}")
    # BG.player_turn()
    BG.dealer_turn()
    print(f"dealer hand: {BG.dealer_hand}, player hand: {BG.player_hand}")
    print(f"dealer value: {BG.dealer_hand.calculate_value()}, player value: {BG.player_hand.calculate_value()}")
    BG.check_winner()
    print(BG.player.balance)