from random import randint

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Game(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guess Game")
        self.resizable(False, False)
        self.start()
        self.computer_guess = randint(1, 1000)

    def guess(self):
        self.count: int = 0
        try:
            user_guess = int(self.entry.get())
            if user_guess == self.computer_guess:
                self.withdraw()
                info = CTkMessagebox(title="Correct!", message=f"You guessed it! You needed {self.count} tries",icon='check')
                info.bind("<Button-1>", lambda e: self.destroy())
            elif user_guess < self.computer_guess:
                self.count += 1
                CTkMessagebox(title="Error", message="Too low!",icon='warning')
            else:
                self.count += 1
                CTkMessagebox(title="Error", message="Too high!",icon='warning')
        except ValueError:
            CTkMessagebox(title="Error", message="Invalid input!",icon='cancel')

    def game(self):
        self.frame_2 = ctk.CTkFrame(self)
        self.frame_2.pack()

        self.label = ctk.CTkLabel(self.frame_2, text="Take a guess")
        self.label.pack()

        self.entry = ctk.CTkEntry(self.frame_2)
        self.entry.pack()

        self.button = ctk.CTkButton(self.frame_2, text="Check", command=self.guess)
        self.button.pack()

    def start(self):
        self.frame_1 = ctk.CTkFrame(self)
        self.frame_1.pack()

        self.label = ctk.CTkLabel(self.frame_1, text="Welcome to the Guess Game")
        self.label.pack()

        self.button = ctk.CTkButton(self.frame_1, text="Click to start", command=lambda: (self.frame_1.destroy(), self.game()))
        self.button.pack()

process = Game()
process.mainloop()
