from blackjack_game import BlackjackGame

class BlackjackController:
    """
    Controller class for BlackjackGame
    """
    def __init__(self, gui):
        self.game = BlackjackGame()
        self.gui = gui

    def player_action(self, action):
        if action == "deal":
            self.game.start_new_game()
            self.update_gui()
        elif action == "hit":
            card = self.game.player_hit()
            self.gui.show_card(card)
            self.update_gui()
            if self.game.is_player_bust():
                self.gui.update_display("Player busts! Dealer wins.")
        elif action == "stand":
            self.game.player_stand()
            self.update_gui()
            self.dealer_turn()
        elif action == "double":
            self.game.player_double()
            self.update_gui()
            if self.game.is_player_bust():
                self.gui.update_display("Player busts! Dealer wins.")
            else:
                self.dealer_turn()

    def dealer_turn(self):
        while not self.game.is_dealer_done():
            card = self.game.dealer_hit()
            self.gui.show_card(card)
            self.update_gui()
        if self.game.is_dealer_bust():
            self.gui.update_display("Dealer busts! Player wins.")
        else:
            self.determine_winner()

    def determine_winner(self):
        winner = self.game.determine_winner()
        if winner == "player":
            self.gui.update_display("Player wins!")
        elif winner == "dealer":
            self.gui.update_display("Dealer wins!")
        else:
            self.gui.update_display("It's a tie!")

    def update_gui(self):
        player_hand = self.game.get_player_hand()
        dealer_hand = self.game.get_dealer_hand()
        self.gui.update_display(f"Player: {player_hand} Dealer: {dealer_hand}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    controller = BlackjackController(gui)
    root.mainloop()
