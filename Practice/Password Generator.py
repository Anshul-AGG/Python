import random
import string

# Getting user input
length = int(input('Enter the length of the password: '))
numbers = int(input('How many numbers do you want in your password? '))
symbols = int(input('How many symbols do you want in your password? '))

#validate input
if numbers + symbols > length:
    print("Error, Its greater.")
else:
    letter_count = length - numbers - symbols

    password_char = []
    password_char += random.choices(string.ascii_letters, k = letter_count)
    password_char += random.choices(string.digits, k = numbers)
    password_char += random.choices(string.punctuation , k = symbols)

    random.shuffle(password_char)
    password = ''.join(password_char)
    print(password)
    
