# Libs
import random


# Functions
def setup():
    global doors, copy, car
    doors = [0, 0, 0]
    car = random.randint(0, 2)
    doors[car] = 1
    copy = doors.copy()
    return


def sim(method):
    choice = random.randint(0, 2)
    if method == "swap":
        host = random.randint(0, 2)
        while host in [choice, car]:
            host = random.randint(0, 2)
        del copy[host]
        choice -= 1
        print(doors)
        print(copy[choice])

    else:
        print(doors)
        print(doors[choice])
    return


for x in range(999):
    setup()
    sim("swap")

for x in range(999):
    setup()
    sim("stay")

