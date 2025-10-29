import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Initialize sound
pygame.mixer.init()
pygame.mixer.music.load("Baby i'm yours.mp3")  # Replace with your sound file

# Main game logic
def check_guess():
    guess = int(entry.get())
    if guess == num:
        pygame.mixer.music.play()
        messagebox.showinfo("Result", f"✅ Correct! The number was {num}")
        root.destroy()
    elif guess < num:
        messagebox.showinfo("Hint", "📉 Too low!")
    else:
        messagebox.showinfo("Hint", "📈 Too high!")

# Setup
num = random.randint(1, 10)
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

# Widgets
label = tk.Label(root, text="Guess a number between 1 and 10:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=check_guess)
button.pack(pady=10)

root.mainloop()
