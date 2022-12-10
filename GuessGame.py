import random


def guess():
    print("TRY TO GUESS NUMBER!!")
    difficulty = int(input("Guess number from 1 to 101: "))
    generate_number = random.randint(1, difficulty)
    return generate_number




secret_number = guess()
def play():

    while True:
        guess1 = input("Enter your guess: ")
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
