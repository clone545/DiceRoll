"""Small script to generate dice rolls"""

from random import randint

def roll(sides, times):
    if times <= 0 or sides <= 0:
        print("You can't do that!")
        return False

    while times > 0:
        print("You rolled a %s" % randint(1,sides))
        times -= 1
    return roll

roll(int(input("How many sides does your dice have?: ")),int(input("How many die need to be cast?: ")))