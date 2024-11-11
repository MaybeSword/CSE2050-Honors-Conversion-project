from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        return card

    def calculate_value(self):
        val = 0
        L_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        face_cards = ['J', 'Q', 'K']
        for card in self.cards:
            if card.rank in L_nums:
                val += card.rank
            elif card.rank in face_cards:
                val += 10
            else: 
                val += 11
                if val > 21:
                    val -= 10
        return val

    def split(self):
        newHand = Hand()
        newHand.add_card(self.cards[1])
        self.cards.pop(1)
        return newHand, self

    def __repr__(self):
        return f"hand: {self.cards}"

