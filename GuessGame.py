import random


def guess():
    print("TRY TO GUESS NUMBER!!")
    difficulty = int(input("Choose difficult from 1 to 101: "))
    generate_number = random.randint(1, difficulty)
    print(generate_number)
    return generate_number


secret_number = guess()


def play():
    while True:
        guess1 = input("Enter your guess or enter Quit to exit: ")
        if guess1 == "quit":
            print("Thanks for playing!")
            break
        elif int(guess1) == secret_number:
            print("You got it!!!")
            break
        elif int(guess1) < secret_number:
            print("Try again, too low:")
        elif int(guess1) > secret_number:
            print("Try again, too high:")


play()
