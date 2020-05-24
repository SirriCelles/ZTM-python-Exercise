# generate a number from 1~10
# get input from user
# check that the input is a number from 1~10
#check is the nymber is the right guess. otherwise
# ask again

# import random
from random import randint
import sys

# rand_num = random.randint(1, 10)

rand_num = randint(1, 10)
# user_num = int(input('Enter a random number 1 to 10 : '))
# if 1 <= user_num <= 10:
#     while user_num != rand_num:
#         print('Try again \n')
#         user_num = int(input('Enter a random number 1 to 10 : '))
#     else:
#         print(f"U guessed the right number {rand_num}. You are a Genius!")


# solution 2
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
