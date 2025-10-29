import sys
import time

def print_lyrics():
    lines = [
        ("These tears mean I'm lettin' you go", 0.2, 1),
        ("I'm learnin' how to be alone", 0.28, 1),
        ("I'm broken, but give it time", 0.27, 1),
        ("I'm gon' be alright", 0.35, 1),
        ("These tears mean it's sittin' in", 0.45, 1),
        ("That I'm not gon' see you again", 0.35, 1),
        ("Til one day in another life", 0.2, 1),
        ("I'm gon' be al-, I'm gon' be alright", 0.4, 1)
    ]

    delays = [0.2, 0.28, 0.2, 0.27, 0.35, 0.45, 0.35, 0.2, 0.4]

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