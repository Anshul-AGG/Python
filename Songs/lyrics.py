import sys
import time
from rich import print
from rich.console import Console
from rich.text import Text
from rich.progress import Progress, BarColumn, TimeElapsedColumn

console = Console()

def print_lyrics():
    lines = [
        ("[bold magenta]I wanna da-", 0.06, 1),
        ("[bold cyan]I wanna dance in the lights", 0.05, 1),
        ("[bold magenta]I wanna ro-", 0.07, 1),
        ("[bold cyan]I wanna rock your body", 0.08, 1),
        ("[bold magenta]i wanna go-", 0.08, 1),
        ("[bold cyan]I wanna go for a ride", 0.28, 1),
        ("[bold yellow]Hop in the music and", 0.07, 1),
        ("[bold green]Rock your body", 0.08, 1),
        ("[bold red]Rock that body", 0.069, 1),
        ("[bold blue]come on, come on", 0.035, 1),
        ("[bold red]Rock that body", 0.05, 1),
        ("[bold green](Rock your body)", 0.03, 1),
        ("[bold red]Rock that body", 0.049, 1),
        ("[bold blue]come on, come on", 0.035, 1),
    ]

    delays = [0.06, 0.05, 0.07, 0.08, 0.08, 0.68, 0.07, 0.08, 0.069, 0.035, 0.05, 0.03, 0.049, 0.035]

    for i, (line, char_delay, enter_line) in enumerate(lines):
        text = Text.from_markup(line)
        for char in text.plain:
            console.print(char, end="", style=text.style)
            sys.stdout.flush()
            time.sleep(char_delay)
        if enter_line == 1:
            print()
        time.sleep(delays[i])

def replay_with_animation(repeats=3):
    for i in range(repeats):
        print_lyrics()
        print(f"\n[bold white on black]--- Replay {i+1} Complete ---\n")
        with Progress(
            "[progress.description]{task.description}",
            BarColumn(),
            TimeElapsedColumn(),
            transient=True,
        ) as progress:
            task = progress.add_task("[cyan]Preparing next replay...", total=100)
            for _ in range(100):
                time.sleep(0.015)
                progress.update(task, advance=1)

# Run with animation
replay_with_animation()