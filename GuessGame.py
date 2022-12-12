from random import randint

difficulty = int(input("Choose number from 1 to 100 to generate difficulty: "))

generate_number = randint(1, difficulty)

# print(generate_number)
print("Lets go! You have 10 attempts")

for play in range(1, 11):
    get_guess_from_user = int(input("Write number: "))

    if get_guess_from_user > generate_number:
        print("To much!")
    elif get_guess_from_user < generate_number:
        print("To low!")
    else:
        print(f"You WIN for in {play} attempt")
        break
    print(f"You used {play} attempt")
else:
    print(f"You waste all attempts. The number was {generate_number}")



input('Press ENTER to Start')