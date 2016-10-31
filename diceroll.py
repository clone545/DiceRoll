"""Small script to generate dice rolls"""

from random import randint

def roll(times):
    if times == 0:
        print("You can't not roll the dice!")
        return False

    while times > 0:
        print("You rolled a %s" % randint(1,6))
        times -= 1
    return roll

roll(int(input("How many die need to be cast?: ")))