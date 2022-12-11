

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game = int(input("Enter the number of the game you want to play: "))
    if game < 1 or game > 3:
        print("Invalid game number. Please choose a game between 1 and 3.")
        return
    level = int(input("Please choose game difficulty from 1 to 5: "))
    if level < 1 or level > 5:
        print("Invalid difficulty level. Please choose a level between 1 and 5.")
        return
