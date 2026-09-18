import random


def guess():
    computer = random.randint(1, 1000)
    user = int(input("Guess a number between 1 and 1000: "))
    if user > computer:
        print("Too high!")
    elif user < computer:
        print("Too low!")
    else:
        print("You guessed it!")

guess()
