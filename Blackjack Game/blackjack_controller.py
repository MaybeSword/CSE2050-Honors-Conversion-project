from blackjack_game import BlackjackGame
from blackjack_gui import BlackjackGUI

class BlackjackController:
    def __init__(self):
        self.game = BlackjackGame()
        self.gui = BlackjackGUI(self)
        self.gui.run()

    def player_action(self, action):
        if action == "deal":
            pass  # Logic to deal cards
        elif action == "hit":
            pass  # Logic for player hitting
        elif action == "stand":
            pass  # Logic for player standing
