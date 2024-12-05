from blackjack_game import BlackjackGame
from time import sleep

class BlackjackController:
    """
    Controller class for BlackjackGame
    """
    def __init__(self, gui):
        self.game = BlackjackGame()
        self.gui = gui
    
    def bet_game(self, sizing):
        self.game.before_game(sizing)

    def player_action(self, action):
        """Calls the correct player action after their input"""
        if action == "deal":
            self.gui.reset_frames()
            dealercards, playercards = self.game.start_game()
            for card in dealercards.cards:
                self.gui.show_card(card, player=False)
            for card in playercards.cards:
                self.gui.show_card(card, player=True)
            self.game.player_turn("deal")
            self.update_gui("")
            if self.game.player.blackjack == True:
                self.dealer_turn()
        elif action == "hit":
            cardshown = self.game.player_turn("hit")
            self.gui.show_card(cardshown)
            self.update_gui()
            if self.game.player.is_busted() or self.game.player_hand.calculate_value() == 21:
                self.dealer_turn()
        elif action == "stand":
            self.game.player_turn("stand")
            self.update_gui()
            self.dealer_turn()
        elif action == "double":
            cardshown = self.game.player_turn("double")
            if cardshown is not None:
                self.gui.show_card(cardshown)
                self.update_gui()
                self.dealer_turn()
            else:
                self.gui.show_error()

    def dealer_turn(self):
        hand_shown = self.game.dealer_turn()
        self.gui.reset_frames(dealer_only=True)
        for card in hand_shown.cards:
            self.gui.show_card(card, player=False)
        self.update_gui()
        self.determine_winner()

    def determine_winner(self):
        result = self.game.check_winner()
        self.update_gui(text=result)
        self.gui.update_balance(self.game.player.balance)
        if self.game.player.balance == 0:
            self.update_zero_balance()
        # self.gui.update_display(result)

    def update_zero_balance(self):
        self.gui.update_zero()
        self.game.player.balance = 2500

    def update_gui(self, text=None):
        player_hand = self.game.player_hand
        dealer_hand = self.game.dealer_hand
        if text is None:
            self.gui.update_display(f"Player: {player_hand} ({player_hand.calculate_value()}) Dealer: {dealer_hand}")
        else:
            if text == "":
                self.gui.update_display(f"Player: {player_hand} ({player_hand.calculate_value()}) Dealer: {dealer_hand}", text)
            else:
                self.gui.update_display(f"Player: {player_hand} ({player_hand.calculate_value()}) Dealer: {dealer_hand} ({dealer_hand.calculate_value()})", text)

