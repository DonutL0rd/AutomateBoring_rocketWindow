from colorama import Fore as col
from random import randint
from colorama import init
import time
import sys

init(autoreset=True)


def thinking_animation(duration):
    animation = ["Deciding your fate", "Deciding your fate.", "Deciding your fate..", "Deciding your fate..."]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in animation:
            sys.stdout.write('\r' + frame)
            sys.stdout.flush()
            time.sleep(0.5)


def pain():
    print(col.GREEN + 'Welcome to THE TERMINAL')
    while True:
        num1 = randint(1,100)
        print(num1)
        try:
            choice1 = int(input(col.BLUE + "What is the number? (1-100)\n"))
            thinking_animation(5)
            if choice1 == num1:
                pain2()
                break
            elif choice1 != num1:
                sys.stdout.write(col.RED + '\rWRONG!\n')
        except ValueError:
            print(col.RED + 'enter a number stupid')
        except:
            print('ERROR....')
            exit(-1)

def pain2():
    pass


pain()