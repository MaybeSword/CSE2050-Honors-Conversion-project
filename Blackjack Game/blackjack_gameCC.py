from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand

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
        self.wins = 0
        self.losses = 0
        self.games = 0
    
    def before_game(self):
        """Betting phase. Use optimal betting techniques."
        """
        self.player.betCC(self.deck)

    def start_game(self):
        """Initial phase of game. First four cards dealt.
        """
        self.player.busted, self.dealer.busted, self.player.blackjack, self.dealer.blackjack = False, False, False, False
        self.dealer.hand = Hand()
        self.player.hand = Hand()
        self.dealer.hand.add_card(self.deck.deal(faceup=False))
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())

    def player_turn(self):
        """Optimal counting cards algorithm's turn to play.
        """
        self.player.playCC(self.deck, self.dealer)

    def dealer_turn(self):
        """Dealer's turn in Blackjack.
        """
        self.dealer.hand.cards[0].faceup = True
        if not self.player.busted:
            self.dealer.play_turn(self.dealer.hand, self.deck)
        

    def check_winner(self):
        """Checks the winner of the hand. 
        """
        self.games+=1
        if self.player.blackjack:
            if self.dealer.blackjack:
                return "It's a tie!"
            else:
                self.player.update_balance(loss=False, blackjack=True)
                self.wins+=1
                return "Player wins + blackjack!"
        elif self.dealer.blackjack and self.player.hand.calculate_value() == 21:
            self.player.update_balance(loss=True)
            self.losses+=1
            return "Dealer wins!"
        elif self.player.is_busted():
            self.player.update_balance(loss=True)
            self.losses +=1
            return "Player busts! Dealer wins."
        elif self.dealer.is_busted():
            self.player.update_balance(loss=False)
            self.wins +=1
            return "Dealer busts! Player wins."
        elif self.dealer.hand.calculate_value() > self.player.hand.calculate_value():
            self.player.update_balance(loss=True)
            self.losses += 1
            return "Dealer wins!"
        elif self.dealer.hand.calculate_value() < self.player.hand.calculate_value():
            self.player.update_balance(loss=False)
            self.wins +=1
            return "Player wins!"
        else:
            return "Push!"

if __name__ == "__main__":
    BG = BlackjackGameCC()
    for i in range(500):
        BG.before_game()
        BG.start_game()
        if i == 488:
            pass
        BG.player_turn()
        BG.dealer_turn()
        BG.check_winner()
    print (f"Wins = {BG.wins}")
    print (f"Losses = {BG.losses}")
    winrate = BG.wins/BG.games
    print (f"Win Rate = {winrate}")
    print (f"Net Profit = {BG.player.balance-500}")
    