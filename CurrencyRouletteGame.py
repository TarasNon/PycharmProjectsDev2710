from currency_converter import CurrencyConverter
import random

difficult = int(input("Choose difficult: "))


def get_money_interval():
    t = CurrencyConverter()
    usd = int(random.uniform(1, 100))
    print(usd, "$")
    con = t.convert(usd, 'USD', 'ILS')
    print(con, "₪")
    high = int(con - (5 - difficult))
    low = int(con + (5 - difficult))
    print(low, high)

    guess = int(input(f"Guess the course of {usd}$ in ILS: "))
    if low <= guess <= high:
        print("True")
    else:
        print("False")



