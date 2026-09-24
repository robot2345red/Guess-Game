from random import randint

import customtkinter as ctk
import matplotlib.pyplot as plt
from CTkMessagebox import CTkMessagebox


class Game(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Guess Game")
        self.geometry("420x130")
        self.resizable(False, False)
        self.count: int = 0
        self.start()

    def save(self, value):

        #For saving datas before displaying with graphics
        with open('results.txt', 'r', encoding='utf-8') as file:
            read = file.readlines()
            if len(read) >= 20:
                read.pop(0)
            elif len(read) == 0:
                read.append(str(value) + '\n')
            else:
                read.append(str(value) + '\n')
        with open('results.txt', 'w', encoding='utf-8') as file:
            file.writelines(read)

    def display_results(self):
        x, y = [], []
        with open('results.txt', 'r') as file:
            read = file.readlines()
            for line in read:
                x.append(int(line))
                y.append(len(x))
        plt.plot(x, y)
        plt.show()

    def difficulty(self, mode):
        MODE = ['easy', 'medium', 'hard', 'very hard']
        if mode not in MODE:
            return CTkMessagebox(title="Error", message=f"Invalid mode: {mode}", icon='cancel')
        match mode:
            case 'easy':
                self.computer_guess = randint(1, 100)
            case 'medium':
                self.computer_guess = randint(1, 1_000)
            case 'hard':
                self.computer_guess = randint(1, 100_000)
            case 'very hard':
                self.computer_guess = randint(1, 1_000_000)
        return self.computer_guess


    def guess(self):
        try:
            user_guess = int(self.entry.get())
            if user_guess == self.computer_guess:
                self.withdraw()
                self.save(self.count)
                info = CTkMessagebox(title="Correct!", message=f"You guessed it! You needed {self.count} tries",
                    icon='check', option_2='Leaderboard')
                if info.get() == 'Leaderboard':
                    self.display_results()
                raise SystemExit
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
        self.frame_2.pack(fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame_2, text="Take a guess")
        self.label.pack()

        self.entry = ctk.CTkEntry(self.frame_2)
        self.entry.pack()

        self.button = ctk.CTkButton(self.frame_2, text="Check", command=self.guess)
        self.button.pack()

    def start(self):
        self.frame_1 = ctk.CTkFrame(self)
        self.frame_1.pack(fill="y", expand=True)

        self.label = ctk.CTkLabel(self.frame_1, text="Welcome to the Guess Game", font=("Arial", 30))
        self.label.pack(fill="both", expand=True)

        self.label_helper = ctk.CTkLabel(self.frame_1, text="(Right click to see what the difficulty means)", font=("Arial", 10))
        self.label_helper.pack(fill="both", expand=True)
        self.label_helper.bind("<Button-3>", lambda e: CTkMessagebox(message="""Mods change the range of random numbers:
        Easy: (1-100)
        Medium: (1-1,000)
        Hard: (1-100,000)
        Very Hard: (1-1,000,000)"""))

        self.button_easy = ctk.CTkButton(self.frame_1, text="Easy",
            command=lambda: (self.frame_1.destroy(), self.difficulty('easy'), self.game()), fg_color="blue")
        self.button_medium = ctk.CTkButton(self.frame_1, text="Medium",
            command=lambda: (self.frame_1.destroy(), self.difficulty('medium'), self.game()), fg_color="green")
        self.button_hard = ctk.CTkButton(self.frame_1, text="Hard",
            command=lambda: (self.frame_1.destroy(), self.difficulty('hard'), self.game()), fg_color="red")
        self.button_impossible = ctk.CTkButton(self.frame_1, text="Very Hard",
            command=lambda: (self.frame_1.destroy(), self.difficulty('very hard'), self.game()), fg_color="#500000")

        self.button_easy.pack_configure(side="left", fill="both", expand=True)
        self.button_medium.pack_configure(side="left", fill="both", expand=True)
        self.button_hard.pack_configure(side="right", fill="both", expand=True)
        self.button_impossible.pack_configure(before=self.button_easy, side="bottom", fill="both", expand=True)

process = Game()
process.mainloop()
