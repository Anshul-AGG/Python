import sys
from rich import print
import time
def print_lyrics():
    lines = [
        ("I wanna da-", 0.06, 1), 
        ("I wanna dance in the lights", 0.05, 1), 
        ("I wanna ro-", 0.07, 1),
        ("I wanna rock your body", 0.08, 1), 
        ("i wanna go-",0.08, 1), 
        ("I wanna go for a ride", 0.68, 1), 
        ("Hop in the music and", 0.07, 1), 
        ("Rock your body", 0.08, 1), 
        ("Rock that body", 0.069, 1), 
        ("come on, come on", 0.035, 1), 
        ("Rock that body", 0.05, 1), 
        ("(Rock your body)", 0.03, 1), 
        ("Rock that body", 0.049, 1), 
        ("come on, come on", 0.035, 1), 

    ]

    delays = [0.06, 0.05, 0.07, 0.08,0.68, 0.07, 0.08, 0.69, 0.035, 0.05, 0.03, 0.049, 0.035]
    for i, (line, char_delay, enter_line) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(char_delay)
        if enter_line == 0:
            print("", end="")
        else:
            print()
        time.sleep(delays[i])
    print_lyrics()