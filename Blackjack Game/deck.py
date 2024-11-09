from card import Card
import random
from hand import Hand

class Deck:
    def __init__(self):
        L_suits = ['clubs', 'spades', 'hearts', 'diamonds']
        L_ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.cards = []
        for rank in L_ranks:
            for suit in L_suits:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)
        self._len = 52

    def __len__(self):
        return self._len

    def deal(self):
        Card_dealt = self.cards[len(self) - 1]
        self.cards.pop(len(self)-1)
        self._len -= 1
        return Card_dealt


if __name__ == "__main__":
    D1 = Deck()
    dealer_hand = Hand()
    player_hand = Hand()
    for i in range(2):
        dealer_hand.add_card(D1.deal())
        player_hand.add_card(D1.deal())
    while dealer_hand.calculate_value() <= 16:
        dealer_hand.add_card(D1.deal())
    for card in dealer_hand.cards:
        print(f"dealer card: {card}")
    for card in player_hand.cards:
        print(f"player card: {card}")

    print(dealer_hand.calculate_value())
    print(player_hand.calculate_value())