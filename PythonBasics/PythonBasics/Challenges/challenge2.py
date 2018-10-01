#Write a program to guess a number between 1 and 10.

import random

highest = 10
randomNumber = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess!= randomNumber:
    guess = int(input())
    if guess < randomNumber:
        print("Please guess higher")
    elif guess > randomNumber:
        print("Please guess lower")
    else:
        print("Well done, you guessed it correctly")