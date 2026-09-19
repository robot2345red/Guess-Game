import random
from tkinter import messagebox

import face

computer = random.randint(1, 1000)

def guess():
    try:
        user = int(face.entry.get())
        if user == computer:
            messagebox.showinfo(title="Success", message="You guessed it!", icon="info")
        elif user > computer:
            messagebox.showinfo(title="Error", message="Too high!", icon="error")
        elif user < computer:
            messagebox.showinfo(title="Error", message="Too low!", icon="error")
    except ValueError:
        messagebox.showinfo(title="Error caused by invalid input", message="Invalid input!", icon="error")


if __name__ == "__main__":
    face.root.mainloop()
