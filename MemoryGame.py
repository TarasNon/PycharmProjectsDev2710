import random
import time


def game():
    generate_number_of_difficulty = int(input("Choose numbers of difficulty from 1 to 101: "))
    generate_sequence = int(input(f"How many numbers you want to remember to {generate_number_of_difficulty}: "))
    rand_list = []

    for i in range(0, generate_sequence):
        rand_list.append(random.randint(1, generate_sequence))
    print(rand_list)

    time.sleep(0.7)
    for i in range(0, 100):
        print('')

    for i in range(0, generate_sequence):
        print("Enter number you remember")
        guess = int(input())
        if guess == rand_list[i]:
            print("Good")
        else:
            print("Bad")
            break



game()