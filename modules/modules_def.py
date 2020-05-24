from modules import utility
import shopping.shopping_cart
# import shopping.more_shopping.shopping_cart
from shopping.more_shopping.shopping_cart import buy
import random
import sys

my_list = [1, 2, 3, 4, 5]

print(utility)
print(shopping.shopping_cart.buy('apple'))
print(buy('banana'))
# prints a random number between 0 and 1
print(random.random())

# prints a random number between the specified intergers
print(random.randint(2, 10))
print(random.randrange(0,20,1))
print(random.choice((1,2,3,4,5)))

random.shuffle(my_list)
print(my_list, '\n')

print(sys, '\n')

