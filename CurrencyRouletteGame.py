from forex_python.converter import CurrencyRates
import random
from datetime import date


def get_money_interval():
    difficult = int(input('Choose difficult: '))
    t = CurrencyRates()

    usd = int(random.randint(1, 100))
    t.convert(usd, 'ILS')
    print(t)

    result = usd * t
    low = int(result - (5 - difficult))
    high = int(result + (5 - difficult))
    print(t)
    #
    return usd, t, low, high


#
#
# def get_guess_from_user(usd):
#     # User needs to guess the Value to a given amount of USD
#     while True:
#         try:
#             guess = int(input(f"Guess the value of {usd}$ in ILS: "))
#         except ValueError:
#             print("Error: Enter just numbers please, not letters, words ,etc...")
#             continue
#         return guess
#

#
# # def play(difficulty):
# #     # Will call all other functions to start the game
# #     usd, t, low, high = get_money_interval(difficulty)
# #     guess = get_guess_from_user(usd)
# #     os.system('cls' if os.name == 'nt' else 'clear')
# #     if high >= guess >= low:
# #         return True
# #     else:
# #         return False

get_money_interval()
