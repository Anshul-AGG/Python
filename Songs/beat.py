import sys
import time
from rich import print

def print_lyrics():
    # Tempo: 125 BPM → 1 beat ≈ 0.48 seconds
    beat = 60 / 125  # ≈ 0.48 seconds

    lines = [
        ("I wanna da-", 0.06, 1),
        ("I wanna dance in the lights", 0.05, 1),
        ("I wanna ro-", 0.07, 1),
        ("I wanna rock your body", 0.08, 1),
        ("i wanna go-", 0.08, 1),
        ("I wanna go for a ride", 0.08, 1),
        ("Hop in the music and", 0.07, 1),
        # Chorus section with smoother pacing
        ("Rock your body", 0.06, 1),
        ("Rock that body", 0.05, 1),
        ("come on, come on", 0.04, 1),
        ("Rock that body", 0.05, 1),
        ("(Rock your body)", 0.04, 1),
        ("Rock that body", 0.05, 1),
        ("come on, come on", 0.04, 1),
        ("Rock that body", 0.05, 1),
    ]

    delays = [
        beat, beat, beat, 2*beat,
        beat, 3*beat, beat,
        0.45, 0.4, 0.35,
        0.4, 0.35, 0.4, 0.35
    ]

    for i, (line, char_delay, enter_line) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(char_delay)
        if enter_line == 1:
            print()
        time.sleep(delays[i])

#Run once
print_lyrics()