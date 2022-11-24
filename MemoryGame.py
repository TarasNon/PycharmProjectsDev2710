import random
import time

rand_list=[]
generate_sequence = int(input("Choose a difficulty of Game: "))
for i in range(generate_sequence):
    rand_list.append(random.randint(1, 101))
print(rand_list)