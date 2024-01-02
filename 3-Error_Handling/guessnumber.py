#!/usr/bin/python3
Secret_no = 7

while True:
    guess = int(input("Guess a number between 1-10: "))

    if guess == Secret_no:
        print("You guessed it right")
        break
