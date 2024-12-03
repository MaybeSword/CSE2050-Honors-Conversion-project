import tkinter as tk
from tkinter import messagebox
from blackjack_controller import BlackjackController
from PIL import Image, ImageTk
import pyglet, os

class BlackjackGUI:
    """
    GUI class for BlackjackGame.
    Manages the graphical user interface and interacts with the controller.
    """
    def __init__(self, root):
        """
        Initialize the BlackjackGUI.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
        """
        pyglet.font.add_file('PokerInOctoberDemo-Dxm3.otf')
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("800x800")  # Set the default window size to 800x800
        self.root.configure(bg="#35654D")
        
        self.controller = BlackjackController(self)

        self.info_label = tk.Label(self.root, text="Welcome to Blackjack!", font=("PokerInOctoberDemo-Dxm3", 16), fg="white")
        self.info_label.configure(bg = "#35654D")
        self.info_label.pack()

        self.text = tk.Label(self.root, font=("Arial",14), fg="white")
        self.text.configure(bg = "#35654D")
        self.text.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.deal, fg="white")
        self.deal_button.configure(bg="#743430")
        self.deal_button.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit, fg="white")
        self.hit_button.configure(bg="#743430")
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand, fg="white")
        self.stand_button.configure(bg="#743430")
        self.stand_button.pack()

        self.double_button = tk.Button(self.root, text="Double", command=self.double, fg="white")
        self.double_button.configure(bg="#743430")
        self.double_button.pack()

        self.player_cards_frame = tk.Frame(self.root)
        self.text.configure(bg = "#35654D")
        self.player_cards_frame.pack(side=tk.LEFT)

        self.dealer_cards_frame = tk.Frame(self.root)
        self.text.configure(bg = "#35654D")
        self.dealer_cards_frame.pack(side=tk.RIGHT)

        self.card_images = {}
        self.load_card_images()

    def reset_frames(self, dealer_only=False):
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()
        if not dealer_only:
            for widget in self.player_cards_frame.winfo_children():
                widget.destroy()


    def load_card_images(self):
        """
        Load card images from the Cards directory and store them in a dictionary.
        """
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                image_path = os.path.join(os.path.dirname(__file__), f"Cards/{value}_of_{suit}.png")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((100, 150), Image.LANCZOS)
                    self.card_images[f"{value}_of_{suit}"] = ImageTk.PhotoImage(image)
                else:
                    print(f"Image not found: {image_path}")
        image_path = os.path.join(os.path.dirname(__file__), f"Cards/back_of_card.png")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((100, 150), Image.LANCZOS)
            self.card_images[f"back_of_card"] = ImageTk.PhotoImage(image)
        else:
            print(f"Image not found: {image_path}")

    def update_display(self, message, text1=None):
        """
        Update the info label with a message.

        Args:
            message (str): The message to display.
        """
        self.info_label.config(text=message)
        if text1 is not None:
            self.text.config(text=text1)

    def show_card(self, card, player=True):
        """
        Display a card image in the player's or dealer's card frame.

        Args:
            card (str): The card to display (e.g., '2_of_hearts').
            player (bool, optional): True if the card is for the player, False if for the dealer. Defaults to True.
        """
        if not card.faceup:
            label = tk.Label(self.dealer_cards_frame, image = self.card_images["back_of_card"])
            label.image = self.card_images["back_of_card"]
            label.pack(side=tk.RIGHT)
        else:
            card_image = self.card_images[f"{card.rank}_of_{card.suit}"]
            if card_image:
                if player:
                    label = tk.Label(self.player_cards_frame, image=card_image)
                    label.image = card_image  # Keep a reference to avoid garbage collection
                    label.pack(side=tk.LEFT)
                else:
                    label = tk.Label(self.dealer_cards_frame, image=card_image)
                    label.image = card_image  # Keep a reference to avoid garbage collection
                    label.pack(side=tk.RIGHT)
    
    def deal(self):
        """
        Handle the Deal button click event.
        """
        self.controller.player_action("deal")

    def hit(self):
        """
        Handle the Hit button click event.
        """
        self.controller.player_action("hit")

    def stand(self):
        """
        Handle the Stand button click event.
        """
        self.controller.player_action("stand")

    def double(self):
        """
        Handle the Double button click event.
        """
        self.controller.player_action("double")


if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()