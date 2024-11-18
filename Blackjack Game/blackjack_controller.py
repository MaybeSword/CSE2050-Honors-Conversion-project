from blackjack_game import BlackjackGame
from time import sleep

class BlackjackController:
    """
    Controller class for BlackjackGame
    """
    def __init__(self, gui):
        self.game = BlackjackGame()
        self.gui = gui

    def reset(self):
        self.game.reset()

    def player_action(self, action):
        """Calls the correct player action after their input"""
        if action == "deal":
            self.game.start_game()
            self.update_gui()
        elif action == "hit":
            card = self.game.player_turn("hit")
            self.gui.show_card(card)
            self.update_gui()
            if self.game.player.is_busted():
                sleep(2)
                self.gui.update_display("Player busts! Dealer wins.")
        elif action == "stand":
            self.game.player_turn("stand")
            self.update_gui()
            self.dealer_turn()
        elif action == "double":
            self.game.player_turn("double")
            self.update_gui()
            if self.game.player.is_busted():
                sleep(2)
                self.gui.update_display("Player busts! Dealer wins.")
            else:
                self.dealer_turn()

    def dealer_turn(self):
        self.game.dealer_turn()
        self.update_gui()
        if self.game.dealer.is_busted():
            sleep(2)
            self.gui.update_display("Dealer busts! Player wins.")
        else:
            sleep(2)
            self.determine_winner()

    def determine_winner(self):
        self.game.check_winner()
        if self.game.player.blackjack:
            self.gui.update_display("Player wins + blackjack!")
        elif self.game.dealer.blackjack:
            self.gui.update_display("Dealer wins!")
        elif self.game.player.is_busted():
            self.gui.update_display("Dealer wins!")
        elif self.game.dealer.is_busted():
            self.gui.update_display("Player wins!")
        elif self.game.dealer_hand.calculate_value() > self.game.player_hand.calculate_value():
            self.gui.update_display("Dealer wins!")
        elif self.game.dealer_hand.calculate_value() < self.game.player_hand.calculate_value():
            self.gui.update_display("Player wins!")
        else:
            self.gui.update_display("It's a tie!")

    def update_gui(self):
        player_hand = self.game.player_hand
        dealer_hand = self.game.dealer_hand
        self.gui.update_display(f"Player: {player_hand} Dealer: {dealer_hand}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    controller = BlackjackController(gui)
    root.mainloop()
