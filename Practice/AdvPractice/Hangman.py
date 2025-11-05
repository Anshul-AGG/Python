# Hangman: A word-guessing game where the user tries to guess a hidden word letter by letter,
# with a limited number of incorrect guesses.
#  This involves string manipulation, lists, loops, and conditional statements.

import random
words = ['hello', 'great','person', 'meet', 'ladies']
word = random.choice(words)

guessed = []
tries = 6
display = ['_' for _ in word]

print("Welcome to game..")
print("Guess the word: ", ' '.join(display))

while tries > 0 and '_' in display:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("enter only a single aplphabet: ")
        continue
    if guess in guessed:
        print('You guessed already.')
        continue

    guessed.append(guess)

    if guess in word:
        print('Correct')
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong.")
        tries -= 1

    print("words ",' '.join(display))
    print("Remaining tries are : " , tries)

if '_' not in display:
    print("YOU WON......", word)
else:
    print('YOu lost dummy...', word)



