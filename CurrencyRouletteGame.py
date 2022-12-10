from currency_converter import CurrencyConverter
import random




def get_money_interval():
    difficult = int(input("Choose difficult: "))
    t = CurrencyConverter()
    usd = int(random.uniform(1, 101))

    con = t.convert(usd, 'USD', 'ILS')
    print(con, "₪")
    high = int(con - (5 - difficult))
    low = int(con + (5 - difficult))



    guess = int(input(f"Guess the course of {usd}$ in ILS: "))
    if low <= guess <= high:
        print("True")
    else:
        print("False")



