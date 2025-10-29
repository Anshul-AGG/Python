import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
user_choice = input("Choose rock , paper or scissors ").lower()

print(f'you choose: {user_choice}')
print(f'computer chose: {computer_choice}')

if(user_choice == computer_choice):
    print("tied")
elif(user_choice == 'rock' and computer_choice == 'scissors') or \
    (user_choice == 'paper' and computer_choice == 'rock') or \
    (user_choice == 'scissors' and computer_choice == 'paper'):
    print("you win baby")

else:
    print("Lost")


