from hand import Hand
from deck import Deck
from player import Player

class Dealer:
    def __init__(self, player=Player):
        self.player = player
        self.busted = False

    def is_busted(self):
        return self.busted   

    def play_turn(self, hand, deck=Deck):
        #bulk of logic is happening here, can transfer it where needed
        while hand.calculate_value() <= 16:
            hand.add_card(deck.deal())
        if hand.calculate_value() > 21:
            self.busted = True
        
        
    
if __name__ == "__main__":
    D1 = Deck()
    Player1 = Player()
    Dealer1 = Dealer(Player1)
    Dealer1.play_turn(D1)
