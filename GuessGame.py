import random


def guess():
    print("TRY TO GUESS NUMBER!!")


difficulty = int(input("Choose number from 1 to 50 to generate difficulty: "))
for x in range(difficulty):
    secret_number = x

    if difficulty > 50:
        print("out of range")

generate_number = random.randint(1, int(difficulty))
secret_number = generate_number


def check():
    global difficulty

    if difficulty == secret_number:
        print("You got it!!!")
    elif difficulty < secret_number:
        difficulty = int(input("Try again too low:"))
        check()
    elif difficulty > secret_number:
        difficulty = int(input("Try again too high:"))
        check()


