from random import randint
import sys

rand_num = randint(int(sys.argv[1]), int(sys.argv[2]))
while True:
    try:
        guess = int(input("Guess a number 1~10:  "))
        if 1 <= guess <= 10:
            if guess == rand_num:
                print(f"U guessed the right number {rand_num}. You are a Genius!")
                break
        else:
            print('Your number should be between 1 and 10')
    except ValueError:
        print('Please enter an integer')

