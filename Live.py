name = input("What is you name: ")


def welcome():
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n\n")


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 0.7 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of U D in ILS")

    try:
        number = int(input("Please insert a number between 1 - 3: "))
        while 3 < number or number < 1:
            number = int(input("Please insert a number between 1 - 3: "))
        diff = int(input('Please choose game difficulty from 1 to 5:'))
        while 5 < diff or diff < 1:
            diff = int(input("Please insert a number between 1 - 5: "))
        print("Welcome to the game")
    except:
        print("Choose right number  PLS!")


load_game()
