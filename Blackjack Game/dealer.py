from hand import Hand
from deck import Deck
from player import Player

class Dealer:
    def __init__(self, player=Player):
        self.player = player
        self.hand = Hand()
        self.player_hand = Hand()

    def play_turn(self, deck=Deck):
        #bulk of logic is happening here, can transfer it where needed
        self.hand.add_card(deck.deal())
        self.player_hand.add_card(deck.deal())
        self.hand.add_card(deck.deal(faceup=False))
        self.player_hand.add_card(deck.deal())
        print(self.hand)
        print(self.player_hand)
        self.player.play(deck)
        self.hand.cards[1].faceup = True
        while self.hand.calculate_value() <= 16:
            self.hand.add_card(deck.deal())
        print(self.hand)
        print(self.player_hand)
    
if __name__ == "__main__":
    D1 = Deck()
    Player1 = Player()
    Dealer1 = Dealer(Player1)
    Dealer1.play_turn(D1)
