import random

words = ['hi', 'hello', 'person']
word = random.choice(words)

guessed = []
tries = 6
display = ['_' for _ in word]

print("Welcome to Hangman.")
print("guess the word: " ,' '.join(display))

while tries > 0 and '_' in display:
    guess = input("Enter the letter : ").lower()
    if len(guess) != 1 and not guess.isalpha():
        print("Error choose only 1 alpahabet only")
        continue
    if guess is guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess in word:
        print("correct")
        for i in range (len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong !!")
        tries -= 1  

    print("words ",' '.join(display))
    print("Remaining tries are : " , tries)      
      
if '_' in display:
    print("You lost", word)

else:
    print("You won....", word)
