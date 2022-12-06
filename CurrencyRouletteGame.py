from currency_converter import CurrencyConverter
import random





def get_money_interval():
    difficult = int(input('Choose difficult from 1 to 100: '))
    t = CurrencyConverter()
    usd = int(random.randint(1, 100))
    print(usd, "$")
    con = t.convert(usd, 'USD', 'ILS')
    print(con, "₪")
    high = int(con - (5 - difficult))
    low = int(con + (5 - difficult))
    print(low, high)

    guess = int(input(f"Guess the value of {usd}$ in ILS: "))

    if low <= guess <= high:
        print("True")
    else:
        print("False")


get_money_interval()