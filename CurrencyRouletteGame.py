from currency_converter import CurrencyConverter
import random



def get_money_interval():
    difficult = int(input("Choose difficult from 1 to 101: "))

    t = CurrencyConverter()
    usd = int(random.uniform(1, 101))
    print(usd, "$")
    con = t.convert(usd, 'USD', 'ILS')
    high = int(con - (5 - difficult))
    low = int(con + (5 - difficult))

    guess = int(input(f"Guess how much of {usd}$ in ILS: "))
    if low <= guess <= high:
        print("True")
    else:
        print("False")



