from blackjack_game import BlackjackGame
from time import sleep

class BlackjackController:
    """
    Controller class for BlackjackGame
    """
    def __init__(self, gui):
        self.game = BlackjackGame()
        self.gui = gui

    def player_action(self, action):
        """Calls the correct player action after their input"""
        if action == "deal":
            self.game.start_game()
            self.game.player_turn("deal")
            self.update_gui("")
            if self.game.player.blackjack == True:
                self.dealer_turn()
        elif action == "hit":
            card = self.game.player_turn("hit")
            self.gui.show_card(card)
            self.update_gui()
            if self.game.player.is_busted() or self.game.player_hand.calculate_value() == 21:
                self.dealer_turn()
        elif action == "stand":
            self.game.player_turn("stand")
            self.update_gui()
            self.dealer_turn()
        elif action == "double":
            self.game.player_turn("double")
            self.update_gui()
            self.dealer_turn()

    def dealer_turn(self):
        self.game.dealer_turn()
        self.update_gui()
        self.determine_winner()

    def determine_winner(self):
        result = self.game.check_winner()
        self.update_gui(text=result)
        # self.gui.update_display(result)

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


if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    controller = BlackjackController(gui)
    root.mainloop()
