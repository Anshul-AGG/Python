import random

num = random.randint(0,11)
print(num)
guess = "enter the number which u have guessed between 1 - 10, u have 5 tries..  "
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: Your guess? "))
    attempts += 1

    if(guess == num):
        print(f"Niceely done. Completed in {attempts + 1}")
        break
    elif(guess < num):
        print("too low")
    else:
        print('Too high')
    
if(guess != num):
    print(f'You lost! Correct num was {num}')

