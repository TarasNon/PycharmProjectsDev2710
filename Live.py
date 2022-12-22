import CurrencyRouletteGame
import GuessGame
import MemoryGame
from score import add_score


def welcome():
    name = input("What is you name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n\n")
    return name


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of U D in ILS")

    while True:
        try:
            choose = int(input("Please insert a number between 1 - 3: "))
            while 3 < choose or choose < 1:
                choose = int(input("Please insert a number between 1 - 3: "))
            difficulty = int(input('Please choose game difficulty from 1 to 5:'))
            while 5 < difficulty or difficulty < 1:
                difficulty = int(input("Please insert a number between 1 - 5: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words ,etc...")
            continue
        if choose == 1:
            MemoryGame.play(difficulty)
            if bool(GuessGame) is True:
                add_score(difficulty=difficulty)
        if choose == 2:
            GuessGame.generate_number(difficulty)
            if bool(MemoryGame) is True:
                add_score(difficulty=difficulty)
        if choose == 3:
            CurrencyRouletteGame.get_money_interval(difficulty)
            if bool(CurrencyRouletteGame) is True:
                add_score(difficulty=difficulty)
        return difficulty, choose


welcome()
load_game()
load_game()
load_game()
