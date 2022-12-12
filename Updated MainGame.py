from os import system

name = input("What is you name: ")
print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.")


def load_game():
    games = ["Memory Game", "Guess the Number", "Currency Roulette"]

    for i in range(len(games)):
        print(f"{i + 1}. {games[i]}")

    game_play = int(input("Enter the number of the game you want to play: ")) - 1
    selected_game = games[game_play]

    if selected_game == "Memory Game":
        import MemoryGame
        MemoryGame.play()

    elif selected_game == "Guess the Number":
        import GuessGame

    elif selected_game == "Currency Roulette":
        import CurrencyRouletteGame
        CurrencyRouletteGame.get_money_interval()

    else:
        quit()

    print("Game Over")


load_game()

system("pause")