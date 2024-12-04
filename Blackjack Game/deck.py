from card import Card
import random
from hand import Hand

class Deck:
    """Deck of cards used in Blackjack
    """
    def __init__(self, n=6):
        """Initialize a Deck of Cards containing the cards from n standard decks of cards.

        Args:
            n (int, optional): Number of standard decks to use. Defaults to 6.
        """
        self.cards = []
        self.newDeck(n)
        self.count = 0
        
    
    def newDeck(self, n):
        """Creates a fresh Deck made up of n standard decks of cards.

        Args:
            n (int): Number of standard decks to use.
        """
        L_suits = ['clubs', 'spades', 'hearts', 'diamonds']
        L_ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.cards = []
        for rank in L_ranks:
            for suit in L_suits:
                for i in range(n):
                    self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)
        self._len = 312


    def __len__(self):
        """
        Returns:
            int: Length of Deck.
        """
        return self._len

    def deal(self, faceup=True):
        """Deals a Card from the top of the Deck.

        Args:
            faceup (bool, optional): True if Card is dealt face up, False if dealt face down. Defaults to True.

        Returns:
            Card: The Card dealt.
        """
        Card_dealt = self.cards[len(self) - 1]
        if not faceup:
            Card_dealt.faceup = False
        self.cards.pop(len(self)-1)
        self._len -= 1
        if self._len < 10:
            self.newDeck(6)
        self.update_count(Card_dealt.card_value())
        return Card_dealt
    
    def update_count(self, value):
        """Used for counting cards algorithm. Updates count based on value.

        Args:
            value (int): Value of the card being counted.
        """
        if 2<=value and value<=6:
            self.count+=1#/len(self)*52
        elif value == 10 or value == 11:
            self.count -=1#/len(self)*52



#tests
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

    player_hand = Hand()
    player_hand.cards = [Card(8, 'clubs'), Card(8, 'diamonds')]
    new_hand1, new_hand2 = player_hand.split()
    new_hand1.add_card(D1.deal())
    new_hand2.add_card(D1.deal())
    print(new_hand1)
    print(new_hand2)
    D2 = Deck()
    dic1 = {'A':0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 'J':0, 'Q':0, 'K':0}
    print(len(D2))
    for card in D2.cards:
        dic1[card.rank] +=1
    print(dic1)