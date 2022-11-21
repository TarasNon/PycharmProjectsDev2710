import random
import sys

print("Let's play a guessing game.")

secret_number = int(input("Pick a number between 1 and 50:"))
if guess > 50:
    print("out of range")
    sys.exit(0)
gennum = random.randint(1, 50)
def checkguess():
    global guess
    global gennum
    if guess == gennum:
        print("You got it!!!")
    elif guess < gennum:
        guess = int(input("Try again too low:"))
        checkguess()
    elif guess > gennum:
        guess = int(input("Try again too high:"))
        checkguess()

checkguess()

