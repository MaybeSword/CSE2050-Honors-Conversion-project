import tkinter as tk
from tkinter import messagebox
from blackjack_controller import BlackjackController
from PIL import Image, ImageTk
import os

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        self.root.geometry("800x600")
        
        self.controller = BlackjackController(self)

        self.info_label = tk.Label(self.root, text="Welcome to Blackjack!", font=("Arial", 16))
        self.info_label.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.deal)
        self.deal_button.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack()

        self.double_button = tk.Button(self.root, text="Double", command=self.double)
        self.double_button.pack()

        self.player_cards_frame = tk.Frame(self.root)
        self.player_cards_frame.pack()

        self.dealer_cards_frame = tk.Frame(self.root)
        self.dealer_cards_frame.pack()

        self.card_images = {}
        self.load_card_images()

    def load_card_images(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        for suit in suits:
            for value in values:
                image_path = os.path.join(os.path.dirname(__file__), f"Cards/{value}_of_{suit}.png")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize((100, 150), Image.LANCZOS)
                    self.card_images[f"{value}_of_{suit}"] = ImageTk.PhotoImage(image)
                else:
                    print(f"Image not found: {image_path}")

    def update_display(self, message):
        self.info_label.config(text=message)

    def show_card(self, card, player=True):
        card_image = self.card_images.get(card)
        if card_image:
            if player:
                label = tk.Label(self.player_cards_frame, image=card_image)
                label.image = card_image  # Keep a reference to avoid garbage collection
                label.pack(side=tk.LEFT)
            else:
                label = tk.Label(self.dealer_cards_frame, image=card_image)
                label.image = card_image  # Keep a reference to avoid garbage collection
                label.pack(side=tk.LEFT)

    def deal(self):
        self.controller.player_action("deal")

    def hit(self):
        self.controller.player_action("hit")

    def stand(self):
        self.controller.player_action("stand")

    def double(self):
        self.controller.player_action("double")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()