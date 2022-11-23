import time, random
from threading import Thread


def printt(lines):
    for _ in range(0, lines):
        print()


def printw(string):
    print(string)
    time.sleep(0.5)


def inputfunc():
    time.sleep(20)
    if answer != None:
        return
    print("You were too slow")


lengthstring, points, lives = 6, 0, 3
printw("This program will present you with a string of numbers")
printw("You will have 10 seconds to try and remember the string")
printw("Then, you will have 20 seconds to retype the string")
printw("Each time you correctly answer, the length of the string will increase by 1")
printw("Each time you incorrectly answer, you will be presented with a string of the same length, and lose a life")
printw("After losing 3 lives, you will lose")
printw("Note. The measures to prevent cheating taken in this program are really weak - anyone can cheat.")
printt(3)
_ = input("<Press ENTER to start>")
printw("Let's start!")
while True:
    stringonum = random.randint(10 ** lengthstring, 10 ** (lengthstring + 1) - 1)
    printw("Your string of numbers is:")
    printw(stringonum)
    time.sleep(5)
    printt(1000)
    printw("You have 20 seconds")
    answer = None
    Thread(target=inputfunc).start()
    answer = input()
    if int(answer) == stringonum:
        lengthstring += 1
        printt(2)
        printw("Correct!")
        points += 1
        printt(2)
        time.sleep(2)
        printw("Next round starting soon")
        time.sleep(2)
    else:
        lives -= 1
        printt(2)
        printw("Wrong!")
        time.sleep(2)
        if lives == 0:
            printw("You ran out of lives. You lose.")
            break
        printw("Next round starting soon")
        time.sleep(2)
print("Rounds answered correctly:", points)
