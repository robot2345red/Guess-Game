import tkinter as tk

import guess

root = tk.Tk()
root.resizable(False, False)

label = tk.Label(root, text="Guess Game\nPut the number between 1 and 1000")
label.pack()

entry = tk.Entry(root)
entry.pack(fill='both', expand=True)

button = tk.Button(root, text="Guess",command=guess.guess)
button.pack(fill='both', expand=True)
