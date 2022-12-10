
from MemoryGame import play
from GuessGame import guess
from CurrencyRouletteGame import get_money_interval


name = input("What is you name: ")


def welcome():
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n\n")


welcome()


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of U D in ILS")

    game = input("Enter the number of the game you want to play: ")

    if game == "1":
        play()
    elif game == "2":
        guess()
    elif game == "3":
        get_money_interval()
    else:
        print("Invalid game. Please try again.")


load_game()