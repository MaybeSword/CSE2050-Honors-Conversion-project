import tkinter as tk
from tkinter import messagebox

class BlackjackGUI:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Blackjack Game")

        self.info_label = tk.Label(self.root, text="Welcome to Blackjack!", font=("Arial", 16))
        self.info_label.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.deal)
        self.deal_button.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack()

    def update_display(self, message):
        self.info_label.config(text=message)

    def show_card(self, card):
        messagebox.showinfo("Card", f"You got {card}")

    def deal(self):
        self.controller.player_action("deal")

    def hit(self):
        self.controller.player_action("hit")

    def stand(self):
        self.controller.player_action("stand")

    def run(self):
        self.root.mainloop()
