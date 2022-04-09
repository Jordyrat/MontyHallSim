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


def sim(method, output):
    choice = random.randint(0, 2)
    if method == "swap":
        host = random.randint(0, 2)
        while host in [choice, car]:
            host = random.randint(0, 2)
        del copy[host]
        choice -= 1
        if output == "win":
            return copy[choice]
        return doors, doors[choice]

    else:
        if output == "win":
            return copy[choice]
        return doors, doors[choice]


def getsuccessdata():
    swapsuccess = 0
    staysuccess = 0
    for x in range(999):
        setup()
        swapsuccess += sim("swap", "win")

    for x in range(999):
        setup()
        staysuccess += sim("stay", "win")

    results = []
    results.append(swapsuccess)
    results.append(staysuccess)
    return results
