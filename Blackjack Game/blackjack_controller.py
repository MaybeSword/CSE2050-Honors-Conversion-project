from blackjack_game import BlackjackGame
from blackjack_gui import BlackjackGUI

class BlackjackController:
    """
    Controller class for BlackjackGame
    """
    def __init__(self):
        self.game = BlackjackGame()
        self.gui = BlackjackGUI(self)
        self.gui.run()

    def player_action(self, action):
        if action == "deal":
            pass  
        elif action == "hit":
            pass  
        elif action == "stand":
            pass  
