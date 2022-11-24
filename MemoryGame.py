import random
import time


def printw(string):
    print(string)
    time.sleep(0.7)


generate_number_of_difficulty = int(input("Choose numbers of difficulty from 1 to 101: "))


def generate():
    list_diff = []
    generate_sequence = int(input(f"How many numbers you want to remember from {generate_number_of_difficulty}: "))
    for i in range(generate_sequence):
        list_diff.append(random.randint(1, generate_number_of_difficulty))
    print(list_diff)
